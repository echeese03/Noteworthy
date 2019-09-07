from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, make_response, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from Firebase.data_handler import checkUser, addUser, validateUser, getFileList

from extractive_summary import *




app = Flask(__name__)
app.secret_key = b'f233fa457b6c0bc56a9816a7'

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('login')) 
    
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
	return render_template('login.html')
	
@app.route('/signUp', methods = ['POST'])
def signUp():
	
	username = request.form['uname']
	password = request.form['pword']
	
	if checkUser(username):
	
		addUser(username, generate_password_hash(password))
		
		session['username'] = username
		return redirect(url_for('home'))
		
	else:
		flash('Error: Username taken!')
		return redirect(url_for('login'))
	
@app.route('/signIn', methods = ['POST'])
def signIn():
	
	username = request.form['uname']
	password = generate_password_hash(request.form['pword'])
	
	if validateUser(username, password):
		session['username'] = username
		return redirect(url_for('home'))
	else:
		flash('Error: Incorrect username or password!')
		return redirect(url_for('login'))
	

@app.route('/home', methods = ['GET', 'POST'])
def home(username=None, fileList=None):
	
	if request.method == "POST":
		text = request.form['text']
		#img = flask.request.files.get('inputFile', '')
		print(text)
		
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
	
@app.route('/previous', methods = ['GET'])
def previous():
	return render_template('previous.html')


















