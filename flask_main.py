from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, make_response, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from /Firebase/data_handler import checkUser, addUser, validateUser, getFileList

from /Processing import gensim, ltk
from gensim import 



@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('login')) 
    
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
	return render_template('login.html')
	
@app.route('/signUp', methods = ['POST'])
def signUp():
	
	username = request.from['INPUTNAMEHERE']
	password = request.from['INPUTNAMEHERE']
	
	if checkUser(username):
	
		addUser(username, generate_password_hash(password))
		
		session['username'] = username
		return redirect(url_for('home'))
		
	else:
		flash('Error: Username taken!')
		return redirect(url_for('login'))
	
@app.route('/signIn', methods = ['POST'])
def signIn():
	
	username = request.from['INPUTNAMEHERE']
	password = request.from['INPUTNAMEHERE']
	
	if validateUser():
		session['username'] = username
		return redirect(url_for('home'))
	else:
		flash('Error: Incorrect username or password!')
	

@app.route('/home', methods = ['GET', 'POST'])
def home(username=None, fileList=None):
	
	if request.method == "POST":
		text = request.from['INPUTNAMEHERE']
		
		#GET HIGHLIGHT
		summary = generate_summary(text)
		
		#GET KEYWORDS
		kw = get_kw(text)
		
		defDict = {}
		urlDict = {}
		
		for word in kw:
			definition, url = get_definition(word)
			
			defDict[kw] = definition
			urlList[kw] = url
		
		addFile(session['username'], text, summary, defDict, urlDict)
		
		return redirect(url_for('result'))
			
	else:
		return render_template('home.html', username=session['username'], fileList = getFileList(session['username']))
		

	
@app.route('/result/<index>', methods = ['GET'])
def result(index=None):
	return render_template('result.html', index=request.args.get(index))


















