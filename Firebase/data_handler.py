import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("noteworthy-bddb5-firebase-adminsdk-x90j4-c1d5d93243.json")
firebase_admin.initialize_app(cred, {'databaseURL' : 'https://noteworthy-bddb5.firebaseio.com'})

ref = db.reference('/')
ref.set({
	'users': [
	
	{'username': 'user1',
	'password': 'pass1',
	'files': [
		{'finalText' : 'finalTextHere',
		'sentiment' : 'happy',
		'abstractText' : 'textHere'},
		
		{'finalText' : 'finalTextHere',
		'sentiment' : 'happy',
		'abstractText' : 'textHere'}
		
		]
	},
	
	{'username': 'user1',
	'password': 'pass1',
	'files':
		[
		{'finalText' : 'finalTextHere',
		'sentiment' : 'happy',
		'abstractText' : 'textHere'},
		
		{'finalText' : 'finalTextHere',
		'sentiment' : 'happy',
		'abstractText' : 'textHere'}
		
		]
	}]

})