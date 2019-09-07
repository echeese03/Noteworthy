import warnings
warnings.simplefilter("ignore", UserWarning)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


from nltk import sent_tokenize
from nltk.stem import WordNetLemmatizer

import matplotlib.pyplot as plt

import numpy as np
from PyDictionary import PyDictionary
import wikipedia
import re



client = language.LanguageServiceClient()
dictionary = PyDictionary()
lemmatizer = WordNetLemmatizer()

def get_tags(text):
    global client

    document = types.Document(
        content = text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)
    categories = response.categories

    catList = [category.name for category in categories]
    
    return catList
    
    

def get_definition(word):
    global dictionary
    #print(word)
    try:
        definitions = dictionary.meaning(word)
        for key, value in definitions.items():
            r =  value[0]
            if(r.count("(") > r.count(")")):
                r += ")"
            return r
    except:
        return get_definition_wiki(word)

def get_definition_wiki(word):
    #print(word)
    try:
        try:
            s = wikipedia.summary(word)
        except:
            pages = wikipedia.search(word)
            s = None
            counter = 0
            while s is None and counter < len(pages):
                try:
                    s = wikipedia.summary(pages[counter])
                    word = pages[counter]
                except:
                    counter += 1
                    pass

            if(s is None):
                return "Keyword not found..."
                    
        summary = re.sub("[\[].*?[\]]", "",str(s.encode("utf-8")))
        summary = re.sub(r'\([^)]*\)', "", summary)
        #words = summary.split(" ")
        sentences = sent_tokenize(summary)

    except IndexError:
        return "Keyword not found..."

    final = ""
    for i in range(min(len(sentences), 2)):
        final += sentences[i].strip() + " "

    url =  wikipedia.page(word).url

    return final.replace("  ", " ").strip().replace("\n", "")[2:]


def get_keywords(text):
    global client, lemmatizer

    document = types.Document(
        content = text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    #print(response)

    num_words = max(min(int(len(sent_tokenize(text)) / 5 * 2), 3), 1)

    kw = []
    forbidden = []
    definitions = []

    limit = False

    for i,e in enumerate(response.entities):
        if i + 1> num_words:
            limit = True
        if(lemmatizer.lemmatize(e.name.lower()) not in forbidden) and limit == False:
            forbidden.append(lemmatizer.lemmatize(e.name.lower()))
            kw.append(e.name.lower())

        if(limit):
            if(e.name[0] != e.name[0].lower() and lemmatizer.lemmatize(e.name.lower()) not in forbidden):
                forbidden.append(lemmatizer.lemmatize(e.name.lower()))
                kw.append(e.name.lower())
                
            

    for w in kw:
        if(len(w.split(" ")) > 1):
            d = get_definition_wiki(w)
        else:
            d = get_definition(w)
        definitions.append(d)
        #print(d)
        #print("-" * 10)
        

    return kw, definitions

def get_sentiment(text):
    global client

    document = types.Document(
        content = text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    return sentiment.score, sentiment.magnitude
    

def graph_text_sentiment(text):
    s_vals = []
    s_x = []
    pos_s_y = []
    pos_s_x = []
    neg_s_y = []
    neg_s_x = []

    sentences = sent_tokenize(text)

    sentences = [ ''.join(x) for x in zip(sentences[0::2], sentences[1::2]) ]

    for i,s in enumerate(sentences):
        score, magnitude = get_sentiment(s)
        if(score >= 0):
            pos_s_y.append(score)
            pos_s_x.append(2 * (i + 1))
        else:
            neg_s_y.append(score)
            neg_s_x.append(2 * (i + 1))
        s_vals.append(score)
        s_x.append(2 * (i + 1))
        #print("Sentence: {}\nScore: {}".format(s, score))

    axes = plt.gca()
    axes.set_ylim([-1.1,1.1])

    plt.plot(s_x, s_vals, color = "black")
    plt.plot(pos_s_x, pos_s_y, "ro")
    plt.plot(neg_s_x, neg_s_y, "ro", color = "blue")
    
    
    plt.xlabel("Sentence Number")
    plt.ylabel("Sentiment")
    plt.title("Sentiment Analysis")

    plt.savefig('plot.png', bbox_inches='tight')






