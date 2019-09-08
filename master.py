from .google_cloud_vision import image_to_text
from .google_cloud_nlp import get_tags, get_keywords, graph_sentiment

from .extractive_summary import generate_summary
from .run import abstractive_summary

import readability

import io
import os

def master_text(text):
    #get extractive
    ex = generate_summary(text)

    #print("Finished Extractive Summary")

    #get abstractive
    fn = os.path.join(os.path.dirname(__file__), './story/a.story')

    with open(fn, 'w') as f:
        f.write(text)
        
    ab = abstractive_summary()

    #print("Finished Abstractive Summary")
    
    #get keywords
    kw, definitions = get_keywords(text)

    #print("Finished getting keywords")

    #other data
    tags = get_tags(text)

    #print("Finished getting tags")
    
    n = graph_sentiment(text)

    #   print("Finished graphing sentiment")
    
    results = readability.getmeasures(text, lang='en')
    r = str(results['readability grades']['Kincaid']/2)
    t = float(r)


    if(t > 90):
        r += " - Very easy to read. Easily understood by an average 11-year-old student."
    elif(t > 80):
        r += " - Easy to read. Conversational English for consumers."
    elif(t > 70):
        r += " - Fairly easy to read"
    elif(t > 60):
        r += " - Plain English. Easily understood by 13- to 15-year-old students."
    elif(t > 50):
        r += " - Fairly difficult to read."
    elif(t > 30):
        r += " - Difficult to read."
    else:
        r += " - Very difficult to read. Best understood by university graduates."

    print([ex, ab, kw, definitions, tags, r, n])

    return [ex, ab, kw, definitions, tags, r, n]


def master_image(imfile):
    return master_text(image_to_text(imfile))
