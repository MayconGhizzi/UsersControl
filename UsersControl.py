import sys
from User import User

def echo(s):
	sys.stdout.write(s+'\n')

echo("welcome to UsersControl")

def switch(opt):
	if opt == 'add':
		user = User(raw_input("username: "),raw_input("email: "));
		switch(raw_input("\n>"));
	else:
		switch(raw_input("WTF your say? do U realy this is a correctly? say help noob\n>"))
	

switch(raw_input(">"));
