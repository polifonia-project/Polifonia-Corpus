import argparse
import os
import csv
from tqdm import tqdm
import pandas as pd
import wikipedia_corpus_reader

def get_indices(lang):
    # synGloss, synType, lemmata, sensekey, wikipediapage, wikidataId
    if lang == 'EN':
        return [0, 1, 2, 3, 11, 12, 24]
    if lang == 'ES':
        return [0, 1, 2, 4, 11, 13, 25]
    if lang == 'NL':
        return [0, 1, 2, 7, 11, 16, 28]
    if lang == 'IT':
        return [0, 1, 2, 6, 11, 15, 27]
    if lang == 'FR':
        return [0, 1, 2, 5, 11, 14, 26]
    if lang == 'DE':
        return [0, 1, 2, 8, 12, 18, 30]


def meta(corpus_folder, langs, output_folder):
    xls_writer = pd.ExcelWriter(os.path.join(output_folder,'wikipedia_corpus_metadata'+'-'.join(langs)+'.xlsx'), engine='xlsxwriter')
    for lang in langs:
        pages, _ = wikipedia_corpus_reader.read(corpus_folder, lang, 'No')
        Rows = []
        with open('/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/metadata/babelnet_lexicon_SynType.tsv') as f:
            reader = csv.reader(f, delimiter='\t')
            rows = [row for row in reader]
        BN = dict()
        indices = get_indices(lang)
        print(len(rows[0]))
        for row in tqdm(rows) :
            BNid, synGloss, synType, lemmasEN, lemmasES, lemmasFR, lemmasIT, lemmasNL, lemmasDE, synCategories, synSources, synWikidata, sensekey, WIKIpageEN, WIKIpageES, WIKIpageFR, WIKIpageIT, WIKIpageNL, WIKIpageDE, WikidataPageEN, WikidataPageES, WikidataPageFR, WikidataPageIT, WikidataPageNL, WikidataPageDE, WikidataIdEN, WikidataIdES, WikidataIdFR, WikidataIdIT, WikidataIdNL, WikidataIdDE = row
            BN[BNid] = [BNid, synGloss, synType, lemmasEN, lemmasES, lemmasFR, lemmasIT, lemmasNL, lemmasDE, synCategories, synSources, synWikidata, sensekey, WIKIpageEN, WIKIpageES, WIKIpageFR, WIKIpageIT, WIKIpageNL, WIKIpageDE, WikidataPageEN, WikidataPageES, WikidataPageFR, WikidataPageIT, WikidataPageNL, WikidataPageDE, WikidataIdEN, WikidataIdES, WikidataIdFR, WikidataIdIT, WikidataIdNL, WikidataIdDE]
        with open(os.path.join(output_folder,'wikipedia_corpus_metadata'+lang+'.tsv'), 'w') as fw:
            writer = csv.writer(fw)
            writer.writerow(['wiki_id', 'bn_id', 'gloss', 'type', 'lemmata', 'sensekey', 'wikipediapage', 'wikidataId'])
            Rows.append(['wiki_id', 'bn_id', 'gloss', 'type', 'lemmata', 'sensekey', 'wikipediapage', 'wikidataId'])
            for page in pages:
                parts = page.split('_')
                wiki_id = parts[0]
                bnid = 'bn:'+parts[-1][:-5]
                try:
                    row = [wiki_id] + [BN[bnid][idx] for idx in indices]
                    row = [r.replace('Optional','').replace('[', '').replace(']','') for r in row]
                except:
                    print(page)
                    continue
                Rows.append(row)
                writer.writerow(row)
            Data = pd.DataFrame.from_records(Rows)
            Data.to_excel(xls_writer, sheet_name=lang, index=False, header=False)
            Data.to_excel(os.path.join(output_folder,'wikipedia_corpus_metadata'+lang+'.xlsx'), index=False, header=False)
    xls_writer.close()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--langs', type=list, default=['DE', 'EN', 'ES', 'FR', 'IT', 'NL'])
    parser.add_argument('--corpus_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus - Data/Polifonia_Wikipedia_Corpus')
    parser.add_argument('--output_folder', type=str, default='/media/rocco/34b2975e-ad76-46e8-b024-3729a4fc15ac/rocco2/rocco/Polifonia Corpus\ -\ Data/Polifonia_Wikipedia_Corpus/Polifonia_Wikipedia_Corpus/metadata')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    meta(args.corpus_folder, args.langs, args.output_folder)