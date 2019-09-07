from gensim.summarization import keywords

def get_kw(text):
    return keywords(text)
