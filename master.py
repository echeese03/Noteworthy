from google_cloud_vision import image_to_text
from google_cloud_nlp import get_tags, get_keywords, graph_sentiment

from extractive_summary import generate_summary
from run import abstractive_summary

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
    
    graph_sentiment(text)

    #   print("Finished graphing sentiment")

    return [ex, ab, kw, definitions, tags]


def master_image(imfile):
    return master_text(image_to_text(imfile))

print(master_image("test.jpg"))
