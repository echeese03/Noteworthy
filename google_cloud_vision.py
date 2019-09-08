import io
import os

from google.cloud import vision
from google.cloud.vision import types

from .extractive_summary import generate_summary
from .google_cloud_nlp import graph_sentiment, get_keywords

import textwrap
from nltk import sent_tokenize

#instantiates a client
client = vision.ImageAnnotatorClient()

def image_to_text(image_file):
        global client
        #annotate the file
        file_name = os.path.join(os.path.dirname(__file__), image_file)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)


        #getting labels:
        labels = client.label_detection(image=image).label_annotations
        topics = [label.description for label in labels]

        if("Text" not in topics):
            print("Please choose an image with text")
            print(topics)
            exit()


        response = client.document_text_detection(image=image)


        text = ""

        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols
                        ])

                        text += word_text.strip() + " "

        #a bit of processing
        sentences = sent_tokenize(text)
        sentences = [s.capitalize() for s in sentences]

        text = " ".join(sentences).strip()

        text = text.replace(" . ", ". ").replace(" , ", ", ").replace(" ; ", "; ").replace(" \' s", "\'s").replace(" “ ", " “").replace(" ” ", "” ")

        return text
