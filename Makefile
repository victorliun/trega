setup:
	virtualenv env
	. env/bin/activate && pip install -r requirements.txt
.PHNOY : setup

clean: 
	rm -rf env
.PHNOY : clean

move: 
	. env/bin/activate && python trega/trello.py
.PHNOY : move
