import argparse
import wikipedia_corpus_reader

def parse(corpus_folder, lang):
    pages = wikipedia_corpus_reader.read(corpus_folder, lang)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--corpus_folder', type=str, default='Polifonia_Wikipedia_Corpus')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    parse(args.corpus_folder, args.lang)