from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, make_response, session, flash
from werkzeug.security import generate_password_hash, check_password_hash



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
	
	if checkUser():
	
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
def home(username=None):
	return render_template('home.html', username=session['username'])
	
	
@app.route('/result', methods = ['GET', 'POST'])
def result():
	return render_template('result.html')