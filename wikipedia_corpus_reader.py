from tqdm import tqdm
import argparse
import os
from bs4 import BeautifulSoup as bs
import spacy

def divide_tokens(text, size):
    tokens = text.split(' ')
    for i in range(0, len(tokens), size):
        yield ' '.join(tokens[i:i+size])

def read(corpus_folder, lang, return_content, limit, nlp):
    Pages = dict()
    pages = [p for p in os.listdir(os.path.join(corpus_folder, lang)) if p.endswith('.html')]
    if limit != 'No':
        pages = pages[:limit]
    if return_content == 'Yes':
        for i, fname in enumerate(tqdm(pages, total=len(pages))):
            with open(os.path.join(corpus_folder, lang, fname)) as f:
                page = bs(f.read(), 'html.parser')
                content = []
                for p in page.findAll('p'):
                    #par = divide_tokens(p.text, 450)
                    #content+= par
                    if len(p.text) > 12:
                        doc = nlp(p.text)
                        content += [sent.text for sent in doc.sents if len(sent.text) > 12]
                    else:
                        continue
            #for par in content:
            #    assert len(par.split(' '))<=450
            Pages[fname] = content
    return pages, Pages

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--corpus_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/Polifonia_Wikipedia_Corpus')
    parser.add_argument('--return_content', type=str, default='No')
    parser.add_argument('--spacy_model', type=str, default='en_core_web_trf')
    parser.add_argument('--limit', type=str, default='No')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    nlp = spacy.load(args.spacy_model, disable=['parser'])
    nlp.add_pipe('sentencizer')
    read(args.corpus_folder, args.lang, args.return_content, args.limit, args.nlp)

