import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import string
import re

def get_sentences(text):
    return sent_tokenize(text)

def tokenize_sentence(s):   
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


   

    
