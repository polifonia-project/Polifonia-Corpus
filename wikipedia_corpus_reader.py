from tqdm import tqdm
import argparse
import os
from bs4 import BeautifulSoup as bs



def read(corpus_folder, lang, return_content, limit):
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
                    content.append(p.text)
            Pages[fname] = content
    return pages, Pages

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--corpus_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/Polifonia_Wikipedia_Corpus')
    parser.add_argument('--return_content', type=str, default='No')
    parser.add_argument('--limit', type=str, default='No')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    read(args.corpus_folder, args.lang, args.return_content, args.limit)

