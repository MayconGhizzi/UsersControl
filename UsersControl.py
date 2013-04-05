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
		
	elif opt == 'help':
		echo('add - add new user')
		echo('list - list current users')
		echo('rm - remove a user')
		echo('export - export users in users.txt in current folder')
		echo('import - import users from users.txt if file exists')
		echo('exit - exit from system')
		switch(raw_input("\n>"));
		
	elif opt == 'exit':
		echo('Goodbye')	
		
	else:
		switch(raw_input("WTF you want? say help nb\n>"))
	

switch(raw_input(">"));
