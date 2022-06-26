import argparse
from tqdm import tqdm
from nltk.corpus import wordnet as wn
import os
from utils.db_utils import *
from collections import Counter
import pickle
import sys
import requests

def annotation2dict(annotation):
    annotation_ = [a.split('\t') for a in annotation]
    annotation_dict = {}
    i=0
    for annotation in annotation_:
        if len(annotation) == 7:
            token_id = 'token_'+str(i)
            annotation_dict.setdefault(token_id, dict())
            annotation_dict[token_id]['form'] = annotation[1]
            annotation_dict[token_id]['lemma'] = annotation[2]
            annotation_dict[token_id]['pos'] = annotation[3]
            annotation_dict[token_id]['offset'] = annotation[4]
            annotation_dict[token_id]['ent_type'] = annotation[5]
            annotation_dict[token_id]['ent_iob'] = annotation[6]
        if len(annotation) == 10:
            token_id = 'token_' + str(i)
            annotation_dict.setdefault(token_id, dict())
            annotation_dict[token_id]['form'] = annotation[1]
            annotation_dict[token_id]['lemma'] = annotation[2]
            annotation_dict[token_id]['pos'] = annotation[3]
            annotation_dict[token_id]['offset'] = annotation[4]
            annotation_dict[token_id]['ent_type'] = annotation[5]
            annotation_dict[token_id]['ent_iob'] = annotation[6]
            annotation_dict[token_id]['entity_mention'] = annotation[7]
            annotation_dict[token_id]['entity_link'] = annotation[8]
            annotation_dict[token_id]['is_musical'] = annotation[9]
        i+=1
    return annotation_dict





def count_sents(conn, lang):
    c = conn.cursor()
    results = c.execute("""SELECT doc_id FROM docs """)
    ndocs = len(list(set(results.fetchall())))
    c = conn.cursor()
    results = c.execute("""SELECT sent_text FROM sents """)
    nsents = 0
    vocab = Counter()
    for i, res in enumerate(results):
        nsents+=1
        vocab.update(res[0].split(' '))
        #if i==100:
        #    break
    print("| " + lang.upper() + " | " + str(ndocs) + " | " + str(nsents)  + " | " + str(len(vocab)) + " | " + str(sum([n for n in vocab.values()])) + " | ")



def stats(annotations_path):
    corpora = ['Pilots']
    langs = ['DE', 'EN', 'ES', 'FR', 'IT', 'NL']
    pilots = ['BELLS', 'CHILD', 'MEETUPS', 'MUSICBO', 'ORGANS']
    for corpus in corpora:
        print(corpus)
        print("| lang |  #documents | #sentences | #types | #tokens |")
        print("| ------ | ------ | ------ | ---------- | --------------- |")
        if corpus != 'Pilots':
            for lang in langs:
                db_path = os.path.join(annotations_path, 'Polifonia_'+corpus+'_Corpus', 'annotations', lang.upper() , corpus.capitalize() + '-' + lang.upper() + '.db')
                conn = create_connection(db_path)
                count_sents(conn, lang)
        else:
            pilot = corpus
            if pilot in ['Child', 'Meetups', 'Musicbo']:
                lang = 'EN'
            if pilot in ['Bells']:
                lang = 'IT'
            if pilot in ['Organs']:
                lang = 'NL'
            for pilot in pilots:
                db_path = os.path.join(annotations_path, 'Polifonia_' + corpus + '_Corpus', 'annotations',
                                       pilot.upper(), corpus.capitalize() + '-' + pilot.capitalize() + '.db')
                #print(db_path)
                conn = create_connection(db_path)
                count_sents(conn, pilot)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations_path', type=str, default='../annotations/db/')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    #--annotations_path /media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia_Corpus_Data/Polifonia_Pilots_Corpus
    stats(args.annotations_path)
