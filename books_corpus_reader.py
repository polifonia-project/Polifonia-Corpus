import argparse
import os
import csv
import pickle
import json_lines
from tqdm import tqdm
from collections import Counter
from utils.db_utils import create_connection
import spacy

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

def read_json(dbpath, limit, nlp):
    Texts = dict()
    books = []
    with json_lines.open(dbpath) as reader:
        for book in tqdm(reader):
            text = book['fullText']
            url = book['id']
            content = []
            for t in text:
                doc = nlp(t)
                content += [sent.text for sent in doc.sents if len(sent.text) > 12]
            Texts[url] = content
            books.append(url)
            #print(url, len(Texts), limit)
            if limit != 'No':
                if len(Texts) == int(limit):
                    break
    return books, Texts



def read_db(database, lang, outpath):
    print('To be adapted')
    # conn = create_connection(database)
    # c = conn.cursor()
    # c.execute('SELECT * FROM books')
    # music = get_music(lang)
    # fpath = os.path.join(outpath, 'books_corpus_metadata' + lang +'.tsv')
    # Counts = dict()
    # Counts[lang] = dict()
    # Counts[lang]['vocab'] = Counter([])
    # Counts[lang]['year'] = Counter([])
    # Counts[lang]['author'] = Counter([])
    # Counts[lang]['publisher'] = Counter([])
    #
    # with open(fpath, 'w') as f:
    #     writer = csv.writer(f, delimiter='\t')
    #     writer.writerow(['url', 'author', 'title', 'year', 'publisher', '#music', '#vocab', '#tokens'])
    #     for book in tqdm(c):
    #         tokens = book[5].lower().split()
    #         vocab = set([t for t in set(tokens)])
    #         inter = len([w for w in tokens if music in w])
    #         if inter > 0:
    #             cc = conn.cursor()
    #             if lang == 'FR':
    #                 cc.execute("SELECT * FROM meta WHERE url = '{0}'".format(book[1]))
    #                 meta = cc.fetchone()
    #                 if meta is not None:
    #                     url, author, title, year, publisher, len_inter, len_vocab, len_tokens =  book[1], meta[2], meta[3], meta[4],meta[6], inter, len(vocab), len(tokens)
    #             if lang == 'ES':
    #                 url, author, title, year, publisher, len_inter, len_vocab, len_tokens = clean_str(book[1]), clean_str(book[2]), clean_str(book[3]), clean_str(book[4]), '', inter, len(vocab), len(tokens)
    #
    #             writer.writerow([url, author, title, year, publisher, len_inter, inter, len_vocab, len_tokens])
    #             Counts[lang]['vocab'].update(tokens)
    #             Counts[lang]['year'].update([year])
    #             Counts[lang]['author'].update([author])
    #             Counts[lang]['publisher'].update([publisher])
    # with open(os.path.join(outpath, 'books_corpus_metadata' + lang +'.pkl'), 'wb') as fw:
    #     pickle.dump(Counts, fw)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--dbpath', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia_Corpus_Data/Polifonia_Books_Corpus/EN/JSTOR-Music-corpus.jsonl')
    parser.add_argument('--return_content', type=str, default='No')
    parser.add_argument('--spacy_model', type=str, default='en_core_web_trf')
    parser.add_argument('--limit', type=str, default='No')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.lang in ['FR', 'ES']:
        read_db(args.dbpath, args.lang, args.output_folder)
    elif args.lang in ['EN']:
        spacy.require_gpu()
        nlp = spacy.load(args.spacy_model, disable=['parser'])
        nlp.add_pipe('sentencizer')
        read_json(args.dbpath, args.limit, nlp)
