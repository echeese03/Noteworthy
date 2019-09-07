import firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from werkzeug.security import generate_password_hash, check_password_hash



# Use the application default credentials
# cred = credentials.Certificate('/Users/ezra/Documents/GitHub/Noteworthy/Firebase/noteworthy-bddb5-firebase-adminsdk-x90j4-162762cb2d.json')
# firebase_admin.initialize_app(cred, {'databaseURL' : 'https://noteworthy-bddb5.firebaseio.com'})

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('/Users/ezra/Documents/GitHub/Noteworthy/Firebase/noteworthy-bddb5-firebase-adminsdk-x90j4-162762cb2d.json') 
    firebase_admin.initialize_app(cred, {'databaseURL' : 'https://noteworthy-bddb5.firebaseio.com'})

db = firestore.client()

#Example write to db
doc_ref = db.collection(u'users').document(u'username')
doc_ref.set({
	u'username': u'user1',
	u'password': u'pass1',
	u'files': [
	{u'definitions': {u'keyword': u'def'},
	u'urls': {u'keyword': u'url'},
	u'finalText': u'finalTextHere',
	u'summary': u'summaryHere'
	}]

})


users_ref = db.collection(u'users')
docs = users_ref.stream()

# for doc in docs:
#      print(u'{} => {}'.format(doc.id, doc.to_dict()))






def checkUser(username):
	if db.collection(u'users').document(u'' + username).get().exists:
		return False
	return True

		
def addUser(username, password):

	doc_ref = db.collection(u'users').document(u''+ username)
	doc_ref.set({
		u'username': u'' + username,
		u'password': u'' + password,
		u'files': []
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
	files =  db.collection(u'users').document(u''+ username).get({u'files'})
	return files
	


def validateUser(username, password):
	if username == db.collection(u'users').document(u''+ username).get({u'username'}) and password == db.collection(u'users').document(u''+ username).get({u'password'}):
		return True
	return False




