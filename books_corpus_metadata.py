import argparse
import os
import csv
import pickle
import json_lines
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

def meta_json(database, lang, outpath):
    fpath = os.path.join(outpath, 'books_corpus_metadata' + lang +'.tsv')
    Counts = dict()
    Counts[lang] = dict()
    Counts[lang]['vocab'] = Counter([])
    Counts[lang]['year'] = Counter([])
    Counts[lang]['author'] = Counter([])
    Counts[lang]['publisher'] = Counter([])
    with open(fpath, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['url', 'author', 'title', 'year', 'publisher', '#music', '#vocab', '#tokens'])
        with json_lines.open(database) as reader:
            for book in reader:
                tokens = [b.lower().split() for b in book['fullText']]
                tokens = [t for sublist in tokens for t in sublist]
                vocab = set([t for t in set(tokens)])
                inter = len([w for w in tokens if 'music' in w])
                author = [b for b in book.keys() if 'author' in b]
                if len(author) != 0:
                    print(author)
                if inter > 0:
                    try:
                        url = book['id']
                    except:
                        url = ''
                    try:
                        url = book['author']
                    except:
                        author = ''
                    try:
                        title = book['title']
                    except:
                        title = ''
                    try:
                        year = book['publicationYear']
                    except:
                        year = ''
                    try:
                        publisher = book['publisher']
                    except:
                        publisher = ''
                    len_inter = inter
                    len_vocab = len(vocab)
                    len_tokens = len(tokens)
                    writer.writerow([url, author, title, year, publisher, len_inter, inter, len_vocab, len_tokens])
                    Counts[lang]['vocab'].update(tokens)
                    Counts[lang]['year'].update([year])
                    Counts[lang]['author'].update([author])
                    Counts[lang]['publisher'].update([publisher])

    with open(os.path.join(outpath, 'books_corpus_metadata' + lang +'.pkl'), 'wb') as fw:
        pickle.dump(Counts, fw)


def meta_db(database, lang, outpath):
    conn = create_connection(database)
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    music = get_music(lang)
    fpath = os.path.join(outpath, 'books_corpus_metadata' + lang +'.tsv')
    Counts = dict()
    Counts[lang] = dict()
    Counts[lang]['vocab'] = Counter([])
    Counts[lang]['year'] = Counter([])
    Counts[lang]['author'] = Counter([])
    Counts[lang]['publisher'] = Counter([])

    with open(fpath, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['url', 'author', 'title', 'year', 'publisher', '#music', '#vocab', '#tokens'])
        for book in tqdm(c):
            tokens = book[5].lower().split()
            vocab = set([t for t in set(tokens)])
            inter = len([w for w in tokens if music in w])
            if inter > 0:
                cc = conn.cursor()
                if lang == 'FR':
                    cc.execute("SELECT * FROM meta WHERE url = '{0}'".format(book[1]))
                    meta = cc.fetchone()
                    if meta is not None:
                        url, author, title, year, publisher, len_inter, len_vocab, len_tokens =  book[1], meta[2], meta[3], meta[4],meta[6], inter, len(vocab), len(tokens)
                if lang == 'ES':
                    url, author, title, year, publisher, len_inter, len_vocab, len_tokens = clean_str(book[1]), clean_str(book[2]), clean_str(book[3]), clean_str(book[4]), '', inter, len(vocab), len(tokens)

                writer.writerow([url, author, title, year, publisher, len_inter, inter, len_vocab, len_tokens])
                Counts[lang]['vocab'].update(tokens)
                Counts[lang]['year'].update([year])
                Counts[lang]['author'].update([author])
                Counts[lang]['publisher'].update([publisher])
    with open(os.path.join(outpath, 'books_corpus_metadata' + lang +'.pkl'), 'wb') as fw:
        pickle.dump(Counts, fw)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='ES')
    parser.add_argument('--dbpath', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/Polifonia_Books_Corpus/BNE_books.db')
    parser.add_argument('--output_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia_Corpus_Data/Polifonia_Books_Corpus/metadata')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.lang in ['FR', 'ES']:
        meta_db(args.dbpath, args.lang, args.output_folder)
    elif args.lang in ['EN']:
        meta_json(args.dbpath, args.lang, args.output_folder)
