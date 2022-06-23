import argparse
import os
import csv
import pickle
from tqdm import tqdm
from collections import Counter
from utils.db_utils import create_connection

def get_music(lang):
    if lang == 'EN':
        return 'music'
    if lang == 'FR':
        return 'musique'
    if lang == 'IT':
        return 'musica'
    if lang == 'ES':
        return 'música'
    if lang == 'DE':
        return 'musik'
    if lang == 'NL':
        return 'muziek'

def clean_str(str):
    return str.replace('\t',' ').strip()



def meta_pkl(database, lang, outpath):
    with open(database, 'rb') as fr:
        Texts = pickle.load(fr)
    fpath = os.path.join(outpath, 'periodicals_corpus_metadata' + lang +'.tsv')

    with open(fpath, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['title', 'year', 'issue n.'])
        for issue, text in tqdm(Texts[1].items()):
            title, issue_n = issue.split('__')
            year = issue_n.split('-')[0]
            n = issue_n.split('-')[1][:-4]
            writer.writerow([title, year, n])



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--dbpath', type=str, default='/media/rocco/3c32f935-c816-48bf-9e60-fa2a31f54d25/rocco/polifonia_corpus/Texts_Periodicals_Spacy_Sents-EN_limit-No.pkl')
    parser.add_argument('--output_folder', type=str, default='/media/rocco/3c32f935-c816-48bf-9e60-fa2a31f54d25/rocco/polifonia_corpus/metadata/')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.lang in ['EN']:
        meta_pkl(args.dbpath, args.lang, args.output_folder)
