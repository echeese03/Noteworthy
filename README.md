## NoteWorthy

Text Summary and Analysis Generator

## Installation

Read the README.txt files in this directory and /logs/myexperiment/train and follow the directions. Make the following environmental variables:
CLASSPATH=full/path/to/stanford-corenlp-3.7.0.jar
GOOGLE_APPLICATION_CREDENTIALS=full/path/to/googlecloudapi/jsonkey

Before running "flask run", execute "export FLASK_APP=flask_main.py"

## What it does
The web app takes in a picture/screenshot of text and auto-generates a summary and highlights important sentences, making skimming a dense article simple. In addition, keywords and their definitions are provided along with some other information (sentiment, classification, and Flesch-Kincaid readability). Finally, a few miscellaneous community tools (random student-related articles and a link to Stack Exchange) are also available.

## How we built it
The natural language processing was split into two different parts: abstractive and extractive.

The abstractive section was carried out using a neural network from [this paper](https://arxiv.org/abs/1704.04368) by Abigail See, Peter J. Liu, and Christopher D. Manning ([Github](https://github.com/abisee/pointer-generator)). Stanford's CoreNLP, was used to chunk and preprocess text for analysis.

Extractive text summarize was done using Google Cloud Language, and the python modules gensim, word2vec and nltk.

We also used Google Cloud Vision API to extract text from an image. To find random student-related articles, we webscraped using BeautifulSoup4.

The front end was built using HTML, CSS, and Bootstrap.

## Challenges we ran into
We found it difficult to parse/chunk our plain-text into the correct format for the neural net to take in. 
In addition, we found it extremely difficult to set up and host our flask app on App Engine/Firestore in the given time; we were unable to successfully upload our model due to our large files and the lack of time. To solve this problem, we decided to keep our project local and use cookies for data retention. Because of this we were able to redirect our efforts towards other features.

## Accomplishments that we're proud of
We're extremely proud of having a working product at the end of a hackathon, especially a project we are so passionate about. We have so many ideas that we haven't implemented in this short amount of time, and we plan to improve and develop our project further afterwards.

## What we learned
We learned how to work with flask, tensorflow models, various forms of natural language processing, and REST (specifically Google Cloud) APIs.

## What's next for NoteWorthy
Although our product is "finished," we have a lot planned for NoteWorthy. Our main goal is to make NoteWorthy a product not only for the individual but for the community (possibly as a tool in the classroom). We want to enable multi-user availability of summarized documents to encourage discussion and group learning. Additionally, we want to personalize NoteWorthy according to the user's actions. This includes utilizing the subjects of summarized articles and their respective reading levels to provide relevant news articles as well as forum recommendations.
