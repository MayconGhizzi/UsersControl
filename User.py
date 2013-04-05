import sys

id = 0

class User(object):	

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.id = self.generateID()
		sys.stdout.write('user sucessfully created: '+str(self.id)+' - '+name+' - '+email)

	def generateID(self):
		global id
		id += 1
		return id
		
	def getLastID(self):
		global id
		return id