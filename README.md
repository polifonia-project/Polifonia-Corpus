
# Polifonia Textual Corpus

> :warning: **Only the English part of the annotations can be downloaded at this stage**

This repository contains the script to access, parse, annotate and interrogate the data and metadata of the Polifonia Textual Corpus.

The high level structure of the repository is the following:

```
Polifonia-Corpus
│   README.md
│   wikipedia_corpus_parser.py
|   wikipedia_corpus_reader.py    
│
└───annotations
│   │   README.md
│   │
│   └───db
│       │   Wikipedia_EN.db
│       │   Periodicals_EN.db
│       │   Books_EN.db
|       |   ........
|       |   "Module"_"Lang".db
│   
└───interrogation
|   │   README.md
|   │   interrogate.py
|   |
|   |___data
|       |   lex_ent_map.pkl
|       |   pages.pkl
|
|___utils
    |   db_utils.py
```

The root folder contains the script to access and parse the Polifonia Corpus data and metadata that are linked in this README.md file.

The annotations folder contains a README.md file in which it is explained how the corpus was annotated. A "db" subfolder of the "annotations" folder is set up to store the databases with the annotations of the corpus that will be used for the interrogations of the corpus. The databases will be downloaded automatically the first time each module will be queried. The links for the download are listed in the "urls.csv" file.

The interrogation folder contains a README.md file that explain how to interrogate the corpus. It contains a "data" subfolder used to link mentions, named entities and Wikipedia page titles.

## The corpus

> :warning: **Only the English part of the annotations are ready at this stage**

The corpus is dived into four modules:
- the Wikipedia module
- the Books module
- the Periodicals module
- the Polifonia Pilots module

Each module (except the Pilot module) contains documents in six languages: Dutch (NL), English (EN), French (FR), German (DE),Italian (IT) and Spanish (ES). 

### The Wikipedia module
It was created selecting from **[BabelNet domains](http://lcl.uniroma1.it/babeldomains/)** all the **[Wikipedia](https://www.wikipedia.org)** musical pages.

#### Metadata
The metadata of the module can be downloaded from:

| lang | tsv                                                                                                                                                                                                                                | xlsx           |    
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| DE   | **[.tsv](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataDE.xlsx?d=w2517edd7efc44c3dae7ad38650fc1c8e&csf=1&web=1&e=FaOeXW)** |  | &#9745; |
| EN   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataEN.tsv?csf=1&web=1&e=pRPo7t)**                                      |  | &#9745; |
| ES   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataES.tsv?csf=1&web=1&e=AdGzJk)**                                      |  | &#9745; |
| FR   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataFR.tsv?csf=1&web=1&e=woKOHY)**                                      |  | &#9745; |
| IT   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataIT.tsv?csf=1&web=1&e=9QWy3S)**                                      |  | &#9745; |
| NL   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataNL.tsv?csf=1&web=1&e=28zhsf)**                                      |  | &#9745; |
| All |                                                                                                                                                                                                                        | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataDE-EN-ES-FR-IT-NL.xlsx?d=wcbd569d8e2c4487c88b3aadc78353be4&csf=1&web=1&e=enjNjj)**|

#### Data

The data of the module can be downloaded from:

| lang | url            | 
|------|----------------|
| DE   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/DE.tar.gz?csf=1&web=1&e=UdFhO5)** |
| EN   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/EN.tar.gz?csf=1&web=1&e=cPKFfg)**       |
| ES   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/ES.tar.gz?csf=1&web=1&e=BeklUc)**       |
| FR   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/FR.tar.gz?csf=1&web=1&e=7sGRRs)**        |
| IT   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/IT.tar.gz?csf=1&web=1&e=K6j6ve)**        |
| NL   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/NL.tar.gz?csf=1&web=1&e=SwP1gK)**        |


#### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #tokens | #types | #links | entities |
|------|------------|------------|---------|---------|------------|---------|
| DE   | 53.986 | 1.459.265 | 44.523.547 | 9.732.779 | 12.561.177 | 2.197.438| 
| EN   | 250.413 | 7.362.272 | 198.257.649 | 1.191.901 | 54.059.979 | 25.786.043 |
| ES   | 57.891 | 1.247.583 | 36.229.557 | 537.465 | 7.171.759 | 2.996.185 |
| FR   | 65.970 | 2.901.295 | 82.979.944 | 653.489 | 19.208.818 | 6.212.997 |
| IT   | 77.986 | 1.548.981 | 47.497.487 | 491.500 | 14.519.636 | 2.649.949 |
| NL   | 36.609 | 1.246.881 | 23.539.528 | 479.962 | 4.716.170 | 2.453.332 |

### The Books module
It was created using the **[Polifonia Textual Corpus Population](https://github.com/polifonia-project/textual-corpus-population)** module that allows to access different digital libraries (such as **[BNF](https://gallica.bnf.fr)** and **[BNE](http://www.bne.es)**) and to select from them documents related to music. The PTCPM allows also to perform optical character recognition (OCR) on images and PDF files. 

#### Metadata
The metadata of the module can be downloaded from:

| lang | .tsv                                                                                                                                                                                  |  
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| DE   | ****                                                                                                                                                                          | **** | 
| EN   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataEN.tsv?csf=1&web=1&e=ZMwthB)** |  
| ES   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataES.tsv?csf=1&web=1&e=h3XUBa)** |  
| FR   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataFR.tsv?csf=1&web=1&e=0svG2v)** |  
| IT   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataIT.tsv?csf=1&web=1&e=THUvPH)** |  
| NL   | ****                                                                                                                                                                          |  
#### Data

The data of the module can not be downloaded due to copyright issue.
However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #tokens |#entities|
|------|------------|------------|---------|---------|
| DE   | http://    | -          | -       | -       |
| EN   | http://    | -          | -       | -       |
| ES   | http://    | -          | -       | -       |
| FR   | http://    | -          | -       | -       |
| IT   | http://    | -          | -       | -       |
| NL   | http://    | -          | -       | -       |

### The Periodicals module
It was created with the help of musicologists that provided the titles of different influencial music periodicals.

#### Metadata
The metadata of the module can be downloaded from:

| lang | url     | 
|------|---------|
| DE   | http:// |
| EN   | http:// |
| ES   | http:// |
| FR   | http:// |
| IT   | http:// |
| NL   | http:// |

#### Data

The data of the module can not be downloaded due to copyright issue.
However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:


| lang | #documents | #sentences | #tokens |#entities |
|------|------------|------------|---------|---------|
| DE   | http://    | -          | -       | -       |
| EN   | http://    | -          | -       | -       |
| ES   | http://    | -          | -       | -       |
| FR   | http://    | -          | -       | -       |
| IT   | http://    | -          | -       | -       |
| NL   | http://    | -          | -       | -       |

### The Polifonia Pilots module
It was created collecting the textual material selected by five **[Polifonia Pilots](https://polifonia-project.eu/pilots/)**:
- BELLS
- CHILD
- MEETUPS
- MUSICBO
- ORGANS

#### Metadata
The metadata of the module can be downloaded from:

| Pilot   | url     | -   |
|---------|---------|-----|
| BELLS   | http:// | - |
| CHILD   | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/Pilots%20Corpora/CHILD/metadata_CHILD.xlsx?d=w74bba036bbf2466fb7e2512abcf8a436&csf=1&web=1&e=IRKX9p)** |
| MEETUPS | http:// | - |
| MUSICBO | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/Pilots%20Corpora/MusicBo/Metadata_MusicBO.xlsx?d=w182957d7cee6459c98e6554d89a6166a&csf=1&web=1&e=BqgKBO)** |
| ORGANS  | http:// | - |


#### Data

The data of some pilot can not be downloaded due to copyright issues. The available data can be foung below:

| Pilot   | url     | - |
|---------|---------|---|
| CHILD   | http:// | - |
| MEETUPS | http:// | - |
| ORGANS  | http:// | - |

However, it is possible to reconstruct the corpus using the metadata provided in the previous section.
Furthermore, the data processed and annotated can be accessed interrogating the corpus (how to interrogate the corpus is explained in a README.md file inside the interrogation folder of this repository).


#### Statistics

Some statistics of the module are provided below:

| lang    | #documents | #sentences | #tokens |#entities|
|---------|------------|------------|---------|---------|
| BELLS   | -          | -          | -       | -       |
| CHILD   | -          | -          | -       | -       |
| MEETUPS | -          | -          | -       | -       |
| MUSICBO | -          | -          | -       | -       |
| ORGANS  | -          | -          | -       | -       |


