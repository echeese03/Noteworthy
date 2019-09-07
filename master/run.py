import os
import json
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk import sent_tokenize

def abstractive_summary():
    os.system("python make_datafiles.py")
    os.system("python run_summarization.py --mode=decode --data_path=finished_files/test.bin --vocab_path=vocab --log_root=logs --exp_name=myexperiment")

    with open('logs/myexperiment/decode/attn_vis_data.json') as json_file:
        data = json.load(json_file)
        text = (TreebankWordDetokenizer().detokenize(data["decoded_lst"]))
        
        text = text.replace(" . ", ". ").replace(" , ", ", ").replace(" ; ", "; ").replace(" \' s", "\'s").replace(" “ ", " “").replace(" ” ", "” ")

        sentences = sent_tokenize(text)
        sentences = [s.capitalize().strip() for s in sentences]

        sentences = list(set(sentences))

        text = " ".join(sentences).strip()
       
        return text
