from gensim.models.keyedvectors import KeyedVectors
from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
from preprocessing import get_sentences, tokenize_sentence
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

def generate_summary(text, top_n = 5):
    summary = []

    sentences = get_text(text)
    

    sim_m = build_matrix(sentences)

    #print(sim_m)

    sim_graph = nx.from_numpy_matrix(sim_m)

    scores = nx.pagerank(sim_graph)

    ranked = []

    for i, s in enumerate(sentences):
        ranked.append((scores[i], s))

    ranked_sentence = sorted(ranked, reverse = True)

    final_sum = ""

    for i in range(top_n):
        final_sum += str(ranked_sentence[i][1]) + " "

    print(final_sum)

print()


s = """In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning. According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, "With AI being the defining technology of our time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That is why it has become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow." The program aims to build up the cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build AI skills."""

generate_summary(s, 5)
    
