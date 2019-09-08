from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, make_response, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import FileStorage

from .Firestore.data_handler import checkUser, addUser, validateUser, getFileList, addFile

from .master import master_text, master_image
from .google_cloud_nlp import get_keywords
from .scrape import random_news_article


app = Flask(__name__)
app.secret_key = b'f233fa457b6c0bc56a9816a7'

@app.route('/', methods=['GET', 'POST'])
def index():
    session["link"] = "<a href = '" + random_news_article() + "'>Beryllium..."
    return redirect(url_for('home')) 
    
	

@app.route('/home', methods = ['GET', 'POST'])
def home(username=None, fileList=None, link="imtired"):
    if request.method == "POST":
        img = request.files.get('inputFile', '').filename
        ex, ab, kw, definitions, tags, r, n = master_image(img)

        session['ex'] = ex
        session['ab'] = ab
        session['readability'] = r
        session['plotnum'] = "<img class='card-img-top' src='\static\plot{}.png'>".format(n)

        final_defs = ""
        for i, k in enumerate(kw):
            final_defs += "<b>" + k.capitalize() + "</b>" + " - " + definitions[i].capitalize() + "<br>"

            session['defs'] = final_defs.strip()
            session['tags'] = ", ".join(tags)[1:]
            print(tags)

        return redirect(url_for('result'))
    else:
        return render_template('home.html', link=session["link"])
	
@app.route('/result', methods = ['GET'])
def result(text="help", ab='its', defs='4', tags='in', readability='the', plotnum = "morning"):
    return render_template('result.html', text=session['ex'], summary=session['ab'], defs=session['defs'], tags=session['tags'], readability=session['readability'], plotnum=session['plotnum'])

@app.route('/previous', methods = ['GET'])
def previous():
    return render_template('previous.html')


















