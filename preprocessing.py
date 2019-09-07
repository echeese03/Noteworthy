import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
from pycontractions import Contractions
import string
import re

cont = Contractions()

def get_sentences(text):
    return sent_tokenize(text)

def tokenize_sentence(s):
    global cont

    s = cont.expand_texts(s, precise = True)
    print(s)

    tokens = word_tokenize(s.lower())

    table = str.maketrans('', '', string.punctuation)
    stripped = []

    stop_words = set(stopwords.words('english'))

    for w in tokens:
        t = w.translate(table)
        if t in stop_words:
            continue
        stripped.append(t)

    return stripped

print(tokenize_sentence("Hello, I know you'll help me"))




   

    
