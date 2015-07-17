#! /usr/local/bin python
from trello import TrelloClient

from config import *


def get_user_stories(board_name, list_name=None):
    client = TrelloClient(TRELLO_API_KEY, TRELLO_API_SECRET,
                          OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    target_board = None
    ret_val = {}
    for board in client.list_boards():
        if board.name == board_name:
            target_board = board
            break
    else:
        ret_val['msg'] = board_name + " Not Found"
        return ret_val

    target_list = None
    for column in target_board.all_lists():
        if column.name == list_name:
            target_list = column
            break
    else:
        ret_val['msg'] = list_name + " Not Found"
        return ret_val

    user_stories = []
    for card in target_list.list_cards():
        card.fetch()
        user_story = {}
        user_story['name'] = card.name
        user_story['desc'] = card.desc
        if card.checklists:
            cl = card.checklists[0]
            user_story['tasks'] = [
                item.name for item in cl.items]

        user_stories.append(user_story)

    ret_val['msg'] = "OK"
    ret_val['user_stories'] = user_stories
    return ret_val


if __name__ == '__main__':
    print get_user_stories('CMP Support (Banthas)', 'Backlog')

