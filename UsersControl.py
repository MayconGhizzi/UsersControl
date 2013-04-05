import sys
from User import User

users = []

def echo(s):
	sys.stdout.write(s+'\n')

echo("welcome to UsersControl")

def switch(opt):
	global users
	
	if opt == 'add':
		user = User(raw_input("username: "),raw_input("email: "));
		users.append(user)
		switch(raw_input("\n>"));
	
	elif opt == 'list':
		for i in range(len(users)):
			user = users[i]
			echo(str(user.id) + ' | ' + user.name + ' | ' + user.email)
		switch(raw_input("\n>"));	
		
	else:
		switch(raw_input("WTF you want? say help nb\n>"))
	

switch(raw_input(">"));
