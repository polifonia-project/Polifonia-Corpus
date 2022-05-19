import argparse
import wikipedia_corpus_reader

def parse(corpus_folder, lang):
    pages = wikipedia_corpus_reader.read(corpus_folder, lang)
    print(len(pages))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, default='EN')
    parser.add_argument('--corpus_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/Polifonia_Wikipedia_Corpus')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    parse(args.corpus_folder, args.lang)