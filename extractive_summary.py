from gensim.models.keyedvectors import KeyedVectors
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
from .preprocessing import get_sentences, tokenize_sentence
import numpy as np
import networkx as nx

model = KeyedVectors.load("word2vec.model")
stop_words = stopwords.words("english")

def get_text(text):
    return get_sentences(text)

def sentence_vector(words):
    global mode, stop_words

    vec = np.zeros((300,), dtype = "float32")
    
    if stop_words is None:
        stop_words = []

    for w in words:
        w = w.replace("\"", "").replace("\'","").strip()
        if w not in stop_words and w in model.vocab:
            vec = np.add(model[w], vec)

    return vec

def similarity(s1, s2):
    s1_av = sentence_vector(tokenize_sentence(s1))
    s2_av = sentence_vector(tokenize_sentence(s2))

    return 1 - cosine_distance(s1_av, s2_av)

def build_matrix(sentences):
    sim_m = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            sim_m[i][j] = similarity(sentences[i], sentences[j])

    return sim_m

def generate_summary(text):
    summary = []

    sentences = get_text(text)

    top_n = max(1, int(len(sentences) / 3))
    

    sim_m = build_matrix(sentences)

    #print(sim_m)

    sim_graph = nx.from_numpy_matrix(sim_m)

    scores = nx.pagerank(sim_graph)

    ranked = []

    for i, s in enumerate(sentences):
        ranked.append((scores[i], s))

    ranked_sentence = sorted(ranked, reverse = True)

    final_sum = []

    for i in range(top_n):
        final_sum.append(ranked_sentence[i][1])

    final = ""

    for s in sentences:
        if(s in final_sum):
            final += "<mark>"  + s + "</mark> "
        else:
            final += s + " "

    return final
    
