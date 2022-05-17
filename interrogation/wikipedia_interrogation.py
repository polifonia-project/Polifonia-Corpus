import argparse
import pickle
from tqdm import tqdm
from nltk.corpus import wordnet as wn

def select_sents_with_keyword(Ann, query, return_content):
    Res = []
    for doc_id, doc in tqdm(Ann.items()):
        for sent_id, sent in doc.items():
            if query in sent['sent']:
                Res.append((doc_id, sent_id, sent['sent']))
    return Res

def get_concept(concepts):
    offset = str(concepts[0].offset())
    while len(offset) < 8:
        offset = '0' + offset
    return 'wn:' + offset + concepts[0].pos()

def select_sents_with_concept(Ann, query, return_content):
    Res = []
    concepts = wn.synsets(query)
    concept = get_concept(concepts)
    for doc_id, doc in tqdm(Ann.items()):
        for sent_id, sent in doc.items():
            if concept in [x['offset'] for x in sent.values() if type(x) == dict and 'offset' in x]:
                Res.append((doc_id, sent_id, sent['sent']))
    return Res


def interrogate(annotations_path, return_content, interrogation_type, query):
    with open(annotations_path, 'rb') as fr:
        Ann = pickle.load(fr)
    if interrogation_type == 'keyword':
        Res = select_sents_with_keyword(Ann, query, return_content)
        print('{} results found'.format(len(Res)))
    elif interrogation_type == 'concept':
        Res = select_sents_with_concept(Ann, query, return_content)
        print('{} results found'.format(len(Res)))
    #for res in Res:
    #    print('\n'.join(res))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annotations_path', type=str, default='/media/4TB/rocco/polifonia_corpus/Annotations_Wikipedia-EN_limit-No.pkl copy')
    parser.add_argument('--return_content', type=str, default='Yes')
    parser.add_argument('--interrogation_type', type=str, default='keyword')
    parser.add_argument('--query', type=str, default='guitar')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    interrogate(args.annotations_path, args.return_content, args.interrogation_type, args.query)
