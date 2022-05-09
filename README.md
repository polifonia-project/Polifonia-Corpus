
# Polifonia Textual Corpus

This repository contains the script to access, parse, annotate and interrogate the data and metadata of the Polifonia Textual Corpus.

The corpus is dived into four modules:
- the Wikipedia module
- the Books module
- the Periodicals module
- the Polifonia Pilots module

Each module (except the Pilot module) contains documents in six languages: Dutch (NL), English (EN), French (FR), German (DE),Italian (IT) and Spanish (ES). 

## The Wikipedia module
It was created selecting from **[BabelNet domains](http://lcl.uniroma1.it/babeldomains/)** all the **[Wikipedia](https://www.wikipedia.org)** musical pages.

### Metadata
The metadata of the module can be downloaded from:

| lang | url                                                                                                                                                                                                                                | url           |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| DE   | **[.tsv](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataDE.xlsx?d=w2517edd7efc44c3dae7ad38650fc1c8e&csf=1&web=1&e=FaOeXW)** | **[.xlsx]()** |
| EN   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataEN.tsv?csf=1&web=1&e=pRPo7t)**                                      | **[.xlsx]()** |
| ES   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataES.tsv?csf=1&web=1&e=AdGzJk)**                                      | **[.xlsx]()** |
| FR   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataFR.tsv?csf=1&web=1&e=woKOHY)**                                      | **[.xlsx]()** |
| IT   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataIT.tsv?csf=1&web=1&e=9QWy3S)**                                      | **[.xlsx]()** |
| NL   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataNL.tsv?csf=1&web=1&e=28zhsf)**                                      | **[.xlsx]()** |
| All | **[.tsv]()**                                                                                                                                                                                                                       | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/metadata/wikipedia_corpus_metadataDE-EN-ES-FR-IT-NL.xlsx?d=wcbd569d8e2c4487c88b3aadc78353be4&csf=1&web=1&e=enjNjj)**||

### Data

The data of the module can be downloaded from:

| lang | url            | - |
|------|----------------|---|
| DE   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/DE.tar.gz?csf=1&web=1&e=UdFhO5)** | - |
| EN   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/EN.tar.gz?csf=1&web=1&e=cPKFfg)**       | - |
| ES   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/ES.tar.gz?csf=1&web=1&e=BeklUc)**       | - |
| FR   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/FR.tar.gz?csf=1&web=1&e=7sGRRs)**        | - |
| IT   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/IT.tar.gz?csf=1&web=1&e=K6j6ve)**        | - |
| NL   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Wikipedia%20corpus/NL.tar.gz?csf=1&web=1&e=SwP1gK)**        | - |


### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #tokens | #types | #links | entities |
|------|------------|------------|---------|---------|------------|---------|
| DE   | 53.986 | 1.459.265 | 44.523.547 | 9.732.779 | 12.561.177 | 2.197.438| 
| EN   | 250.413 | 7.362.272 | 198.257.649 | 1.191.901 | 54.059.979 | 25.786.043 |
| ES   | 57.891 | 1.247.583 | 36.229.557 | 537.465 | 7.171.759 | 2.996.185 |
| FR   | 65.970 | 2.901.295 | 82.979.944 | 653.489 | 19.208.818 | 6.212.997 |
| IT   | 77.986 | 1.548.981 | 47.497.487 | 491.500 | 14.519.636 | 2.649.949 |
| NL   | 36.609 | 1.246.881 | 23.539.528 | 479.962 | 4.716.170 | 2.453.332 |

## The Books module
It was created using the **[Polifonia Textual Corpus Population](https://github.com/polifonia-project/textual-corpus-population)** module that allows to access different digital libraries (such as **[BNF](https://gallica.bnf.fr)** and **[BNE](http://www.bne.es)**) and to select from them documents related to music. The PTCPM allows also to perform optical character recognition (OCR) on images and PDF files. 

### Metadata
The metadata of the module can be downloaded from:

| lang | url          | -             |
|------|--------------|---------------|
| DE   | **[.tsv]()** | **[.xlsx]()** |
| EN   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataEN.tsv?csf=1&web=1&e=ZMwthB)** | **[.xlsx]()** |
| ES   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataES.tsv?csf=1&web=1&e=h3XUBa)** | **[.xlsx]()** |
| FR   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataFR.tsv?csf=1&web=1&e=0svG2v)** | **[.xlsx]()** |
| IT   | **[.tsv](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/metadata/books_corpus_metadataIT.tsv?csf=1&web=1&e=THUvPH)** | **[.xlsx]()** |
| NL   | **[.tsv]()** | **[.xlsx]()** |
### Data

The data of the module can be downloaded from:

| lang | url            | - |
|------|----------------|---|
| DE   | http://        | - |
| EN   | http://        | - |
| ES   | http://        | - |
| FR   | http://        | - |
| IT   | **[tar.gz](https://liveunibo.sharepoint.com/:u:/r/sites/polifonia/Shared%20Documents/WP4/Polifonia%20Corpus/Books%20corpus/IT/txt.tar.gz?csf=1&web=1&e=CL2QIQ)** | - |
| NL   | http://        | - |


### Statistics

Some statistics of the module are provided below:

| lang | #documents | #sentences | #tokens |#entities|
|------|------------|------------|---------|---------|
| DE   | http://    | -          | -       | -       |
| EN   | http://    | -          | -       | -       |
| ES   | http://    | -          | -       | -       |
| FR   | http://    | -          | -       | -       |
| IT   | http://    | -          | -       | -       |
| NL   | http://    | -          | -       | -       |

## The Periodicals module
It was created with the help of musicologists that provided the titles of different influencial music periodicals.

### Metadata
The metadata of the module can be downloaded from:

| lang | url     | - |
|------|---------|---|
| DE   | http:// | - |
| EN   | http:// | - |
| ES   | http:// | - |
| FR   | http:// | - |
| IT   | http:// | - |
| NL   | http:// | - |
### Data

The data of the module can be downloaded from:

| lang | url     | - |
|------|---------|---|
| DE   | http:// | - |
| EN   | http:// | - |
| ES   | http:// | - |
| FR   | http:// | - |
| IT   | http:// | - |
| NL   | http:// | - |


### Statistics

Some statistics of the module are provided below:


| lang | #documents | #sentences | #tokens |#entities |
|------|------------|------------|---------|---------|
| DE   | http://    | -          | -       | -       |
| EN   | http://    | -          | -       | -       |
| ES   | http://    | -          | -       | -       |
| FR   | http://    | -          | -       | -       |
| IT   | http://    | -          | -       | -       |
| NL   | http://    | -          | -       | -       |

## The Polifonia Pilots module
It was created collecting the textual material selected by five **[Polifonia Pilots](https://polifonia-project.eu/pilots/)**:
- BELLS
- CHILD
- MEETUPS
- MUSICBO
- ORGANS

### Metadata
The metadata of the module can be downloaded from:

| Pilot   | url     | -   |
|---------|---------|-----|
| BELLS   | http:// | - |
| CHILD   | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/Pilots%20Corpora/CHILD/metadata_CHILD.xlsx?d=w74bba036bbf2466fb7e2512abcf8a436&csf=1&web=1&e=IRKX9p)** |
| MEETUPS | http:// | - |
| MUSICBO | **[.xlsx](https://liveunibo.sharepoint.com/:x:/r/sites/polifonia/Shared%20Documents/Pilots%20Corpora/MusicBo/Metadata_MusicBO.xlsx?d=w182957d7cee6459c98e6554d89a6166a&csf=1&web=1&e=BqgKBO)** |
| ORGANS  | http:// | - |


### Data

The data of the module can be downloaded from:

| Pilot   | url     | - |
|---------|---------|---|
| BELLS   | http:// | - |
| CHILD   | http:// | - |
| MEETUPS | http:// | - |
| MUSICBO | http:// | - |
| ORGANS  | http:// | - |



### Statistics

Some statistics of the module are provided below:

| lang    | #documents | #sentences | #tokens |#entities|
|---------|------------|------------|---------|---------|
| BELLS   | http://    | -          | -       | -       |
| CHILD   | http://    | -          | -       | -       |
| MEETUPS | http://    | -          | -       | -       |
| MUSICBO | http://    | -          | -       | -       |
| ORGANS  | http://    | -          | -       | -       |


