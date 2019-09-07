import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("noteworthy-bddb5-firebase-adminsdk-x90j4-c1d5d93243.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://noteworthy-bddb5.firebaseio.com'})

#EXAMPLE WRITING TO FILE
# ref = db.reference('/')
# ref.set({
# 	'users': [
# 	
# 	{'username': 'user1',
# 	'password': 'pass1',
# 	'files': [
# 		{'finalText' : 'finalTextHere',
# 		'summary' : 'summaryHERE',
# 		'definitions' : 
#			{'keyword' : 'def'},
#		'urls' : 
#			{'keyword' : 'url'}
#	
#		},
# 		
# 		{'finalText' : 'finalTextHere',
# 		'summary' : 'summaryHERE',
# 		'definitions' : 
#			{'keyword' : 'def'},
#		'urls' : 
#			{'keyword' : 'url'}
#	
#		}
# 		
# 		]
# 	},
# 	
# 	{'username': 'user1',
# 	'password': 'pass1',
# 	'files':
# 		[
# 		{'finalText' : 'finalTextHere',
# 		'summary' : 'summaryHERE',
# 		'definitions' : 
#			{'keyword' : 'def'},
#		'urls' : 
#			{'keyword' : 'url'}
#	
#		},
# 		
# 		{'finalText' : 'finalTextHere',
# 		'summary' : 'summaryHERE',
# 		'definitions' : 
#			{'keyword' : 'def'},
#		'urls' : 
#			{'keyword' : 'url'}
#	
#		}
# 		]
# 	}]
# 
# })

def checkUser(username):
	ref = db.reference('/users')
	snapshot = ref.order_by_child('username').get()
	if username in snapshot.items():
		return false
	else:
		return true
		
def addUser(username, password):
	ref = db.reference('/users')
	ref.push().set({
	'username': username,
	'password': password,
	'files': []
	})

def addFile(username, text, summary, defDict, urlDict):
	ref = db.reference('/users')
	snapshot = ref.order_by_child('username').get()
	index = snapshot.index(username)
	ref = db.reference('/users/' + str(index) + '/files')
	ref.push.set({
		'finalText' : text,
		'summary' : summary,
		'definitions' : defDict,
		'urls' : urlDict
	})
	
def getFileList(username):
	ref = db.reference('/users')
	snapshot = ref.order_by_child('username').get()
	index = snapshot.index(username)
	ref = db.reference('/users/' + str(index))
	snapshot = ref.order_by_child('files').get()
	return snapshot

