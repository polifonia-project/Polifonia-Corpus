import argparse
import csv
from tqdm import tqdm
from nltk.corpus import wordnet as wn
import os
import requests
from db_utils import *
import pandas as pd
import gdown

def annotation2dict(annotation):
    annotation_ = [a.split('\t') for a in annotation]
    annotation_dict = {}
    i=0
    for annotation in annotation_:
        if len(annotation) == 7 or len(annotation) == 10:
            token_id = 'token_'+str(i)
            annotation_dict.setdefault(token_id, dict())
            annotation_dict[token_id]['form'] = annotation[1]
            annotation_dict[token_id]['lemma'] = annotation[2]
            annotation_dict[token_id]['pos'] = annotation[3]
            annotation_dict[token_id]['offset'] = annotation[4]
            annotation_dict[token_id]['ent_type'] = annotation[5]
            annotation_dict[token_id]['ent_iob'] = annotation[6]
            i+=1
    return annotation_dict


def print_sents_concepts(results, query):
    #cols = [column[0] for column in results.description]
    #results = pd.DataFrame.from_records(data=results.fetchall(), columns=cols)
    Results = []
    for result in results:
        res = [result[0], result[1], result[2].split('\n')[2]]
        annotation = annotation2dict(result[3].split('\n'))
        key_concept = [(k, t) for k, t in annotation.items() if t['offset'] == query]
        try:
            annotation_ = list(annotation.values())
            idx = int(key_concept[0][0].split('_')[1])
            print(res[0].ljust(30), ' '.join([annotation_[idx_]['form'] for idx_ in range(idx-8,idx)]).rjust(60), annotation_[idx]['form'].center(10), ' '.join([annotation_[idx_]['form'] for idx_ in range(idx+1,idx+9)]).ljust(60))
            Results.append(res)
        except:
            continue
    return Results


def print_sents(results, query):
    #cols = [column[0] for column in results.description]
    #results = pd.DataFrame.from_records(data=results.fetchall(), columns=cols)
    Results = []
    for result in results:
        res = [result[0], result[1], result[2].split('\n')[2]]
        #print(res[0],  res[1])
        try:
            idx = res[2].split().index(query)
            print(res[0].ljust(30), ' '.join(res[2].split()[idx-8:idx]).rjust(60), query.center(10), ' '.join(res[2].split()[idx+1:idx+9]).ljust(60))
            Results.append(res)
        except:
            continue
    return Results
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #    print(results.to_string)


def save_results(Results, query, type, db):
    with open(os.path.join('out/', '_'.join([db,type,query]) +'.tsv')) as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(Results)


def select_sents_with_keyword(conn, query, sent_n, corpus, save_to_file):
    c = conn.cursor()
    offset = 0
    more = ''
    Results = []
    while more != 'no':
        #results = c.execute("""SELECT doc_id, sent_id, sent_text, sent_annotation FROM sents WHERE sent_text LIKE ? LIMIT ? OFFSET ? """, ('% '+query+' %', sent_n, offset))
        results = c.execute(
            """SELECT doc_id, sent_id, sent_text, sent_annotation, INSTR(sent_text, ?) instr_ FROM sents WHERE instr_ > 0 LIMIT ? OFFSET ? """,
            (' ' + query + ' ', sent_n, offset))

        Results+=print_sents(results, query)
        more = input('Press "enter" for more sentences? (type "no" and press "enter" to stop)')
        offset+=sent_n
    return Results


def get_concept(query, concepts):
    if len(concepts) > 1:
        print('The word {} is associated with {} concepts'.format(query, len(concepts)))
        print('Please select one concept from the list below indicating its number:')
        for i, concept in enumerate(concepts):
            print('{}. {} - {}'.format(i, concept.pos(), concept.definition()))
        index = input()
        concept = concepts[int(index)]
    else:
        concept = concepts[0]
    print('The research is based on the concept defined as:\n{}:\t{}'.format(query, concept.definition()))
    offset = str(concept.offset())
    while len(offset) < 8:
        offset = '0' + offset
    return 'wn:' + offset + concepts[0].pos(), concept

def select_sents_with_concept(conn, query, sent_n, corpus, save_to_file):
    concepts = wn.synsets(query)
    wn_key, concept = get_concept(query, concepts)
    c = conn.cursor()
    offset = 0
    more = ''
    Results = []
    while more != 'no':
        results = c.execute(
        """SELECT doc_id, sent_id, sent_text, sent_annotation, INSTR(sent_annotation, ?) instr_ FROM sents WHERE instr_ > 0 LIMIT ? OFFSET ? """,
        (wn_key, sent_n, offset))
        Results+=print_sents_concepts(results, wn_key)
        more = input('Press "enter" for more sentences? (type "no" and press "enter" to stop)')
        offset+=sent_n
    return Results


def interrogate(annotations_path, corpus, lang, interrogation_type, query, sent_n, save_to_file):
    db_path = os.path.join(annotations_path, corpus.capitalize() + '_' + lang.upper() + '.db')
    if os.path.exists(db_path) == False:
        download_annotations(annotations_path, corpus.capitalize() + '_' + lang.upper())
    conn = create_connection(db_path)
    if interrogation_type == 'keyword':
        Results = select_sents_with_keyword(conn, query, sent_n, corpus, save_to_file)
    elif interrogation_type == 'concept':
        Results = select_sents_with_concept(conn, query, sent_n, corpus, save_to_file)
    if save_to_file == 'Yes':
        save_results(Results, query, 'keyword', corpus)
        print('{} sentences stored'.format(len(Results)))


def download_annotations(annotations_path, db_name):
    db_names = dict()
    with open(os.path.join(annotations_path, 'urls.csv')) as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                continue
            name, lang, url = line.split(',')
            db_names['_'.join([name, lang])] = url

    gdown.download(db_names[db_name], os.path.join(annotations_path, db_name + '.db'), quiet=False)
                # response = requests.get(url, stream=True)
                # total_size_in_bytes = int(response.headers.get('content-lenght', 0))
                # block_size = 1024
                # progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                # with open(os.path.join(annotations_path, '_'.join([name, lang]) + '.db'), 'wb') as f:
                #     for data in response.iter_content(block_size):
                #         progress_bar.update(len(data))
                #         f.write(data)
                # progress_bar.close()
                # if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                #     print('ERROR: something went wrong!')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations_path', type=str, default='../annotations/db/')
    parser.add_argument('--corpus', type=str, default='Wikipedia',
                        help="It can be Wikipedia, Books, Periodicals or Pilots")
    parser.add_argument('--lang', type=str, default='EN', help="It can be DE, EN, ES, FR, IT or NL")
    parser.add_argument('--interrogation_type', type=str, default='concept',
                        help="It can be Keyword, concept or entity")
    parser.add_argument('--query', type=str, default='swing')
    parser.add_argument('--sent_n', type=int, default=50)
    parser.add_argument('--save_to_file', type=str, default='No')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    interrogate(args.annotations_path, args.corpus, args.lang, args.interrogation_type, args.query, args.sent_n, args.save_to_file)
