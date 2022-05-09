
# Annotations of the Polifonia Textual Corpus

This repository contains the annotations of the Polifonia Textual Corpus.

The corpus is dived into four modules:
- the Wikipedia module
- the Books module
- the Periodicals module
- the Polifonia Pilots module

Each module (except the Pilot module) contains documents in six languages: Dutch (NL), English (EN), French (FR), German (DE),Italian (IT) and Spanish (ES).

## Annotation Pipeline

The annotations of the corpus was produced using cutting-edge Natural Language Processing technologies.
We annotated each text of the corpus with a NLP pipeline composed of:

1. Sentece splitting
2. Tokenization
3. Lemmatization
4. Part-of-speech tagging
5. Word Sense Disambiguation
6. Named Entity Recognition
7. Entity Linking

Steps 1-4 and 6 have been conducted using the **[SpaCy](http://spacy.io)** NLP library.
For each language of the corpus we used a dedicated SpaCy Model:

| lang | model name |
|------|------------|
| DE   | de_dep_news_trf |
| EN   | en_core_web_trf |
| ES   | es_dep_news_trf |
| FR   | fr_dep_news_trf |
| IT   | it_core_news_lg |
| NL   | nl_core_news_lg |

Steps 5 and 7 require more sophisticated technologies.
For this reason, we used **[EWISER](https://github.com/SapienzaNLP/ewiser)** for step 5 (Word Sense Disambiguation) for all the languages of the corpus.
For step 7 we used **[ExTenD](https://github.com/SapienzaNLP/extend)** for English and **[mGENRE](https://github.com/facebookresearch/GENRE)** for all other languages of the corpus.

## Annotation Example
The annotations of the Polifonia Textual Corpus are provided in **[CoNLL-U format](https://universaldependencies.org/format.html)**.
Given an input sentence of the corpus such as:

> James H. Mathis Jr. (born August 1967), known as Jimbo Mathus, is an American singer-songwriter and guitarist, best known for his work with the swing revival band Squirrel Nut Zippers.

from the English Wikipedia module, the resulting annotation will start with metadata information:

> id of the document in the corpus
>> #polifonia doc id = 32607842_bn___02615097n.html

> id of the sentence in the corpus
>> #polifonia sent id = sent_0

> Text of the sentence
>> #sent = James H. Mathis Jr. (born August 1967), known as Jimbo Mathus, is an American singer-songwriter and guitarist, best known for his work with the swing revival band Squirrel Nut Zippers. 

Afther that there is the sentence annotation: 

| token_id  | word form  | lemma | POS | WordNet sense | NER class | NER BIO tag | Entity Linking ------- | is a musical concept? |
|-----------|------------|-------|-----|---------------|-----------|-----------|---------------------|-----------------------|
| token_2   | James	    | James	| PROPN	|             | PERSON	  | B	      | James H. Mathis Jr.	 | 	0                    |
| token_3   |  H.	| H.	| PROPN		| | PERSON	| I		| 	0                  | 0                     |
| token_4	  | Mathis	| Mathis	| PROPN	| 	| PERSON	| I		| 	0                  | 0                     |
| token_5	  | Jr.	| Jr.	| PROPN	| 	| PERSON	| I		| 	0                  | 0                     |                                        
| token_6	  | (	| (	| PUNCT	| 	| 	| O		| 	0                  | 0                     |
| token_7	  | born	| bear	| VERB	| wn:02518161v	| 	| O		| 	0                  | 0                     |
| token_8	  | August	| August	| PROPN	| 	| DATE	| B	| August 1967         | 0                     | 		0|
| token_9	  | 1967	1967	NUM		DATE	I			0                                                  |     |     |     |     |     |     |     |
| token_10	 | )	| )	| PUNCT	| 	| 	| O	| 		0                 | 0                     |
| token_11	 | ,	| ,	| PUNCT	| 	| 	| O	| 		0                 | 0                     |
| token_12	 | known| 	know	| VERB	| wn:01426397v	| 	| O	| 		0                 | 0                     |
| token_13	 | as	| as	| ADP	| 		| | O		| 	0                  | 0                     |                                              
| token_14	 | Jimbo	| Jimbo	| PROPN	| 	| PERSON	| B	| Jimbo Mathus	       | 0                     |
| token_15	 | Mathus	| Mathus	| PROPN	| 	| PERSON	| I		| 	0                  | 0                     |
| token_16	 | ,	| ,	| PUNCT	| 	| 	| O		| 	0                  | 0                     |                                       
| token_17	 | is	| be	| AUX	| 		| | O		| 	0                  |  0 |                                                
| token_18	 | an	| an	| DET	| 		| | O		| 	0                  |  0 |
| token_19	 | American	| american	| ADJ	| wn:02927512a	| NORP	| B	| United States	      | 0 |
| token_20	 | singer	| singer	| NOUN	| wn:10599806n	| 	| O	| 	0                  | 	1                  |
| token_21	 | -	| -	| PUNCT		| 	| | O		| 	0                  |  0|                       
| token_22	 | songwriter	| songwriter	| NOUN	| wn:10624540n	| 	| O	| 	0                  | 	1                             |
| token_23	 | and	| and	| CCONJ	| 	| 	| O		| 	0                  |  0 | 
| token_24	 | guitarist	| guitarist	| NOUN	| wn:10151760n	| | 	O | 	0                  | 		1                 |
| token_25	 | ,| 	,	| PUNCT	| 	| | 	O	| 		0                 |  0 |            
| token_26	 | best	| well	| ADV	| wn:00011093r	| 	| O	| 		0                 | 0 |
| token_27	 | known	| know	| VERB	| wn:00596644v	| 	| O	| 		0                 |  0 |
| token_28	 | for	| for	| ADP		| 	|  | O	| 		0                 |  0 |                                            
| token_29	 | his	| his	| PRON		| 	|  | O	| 		0                 |  0 |
| token_30	 | work	| work	| NOUN	| wn:05755883n	| 	| O		| 	0                  | 0 |
| token_31	 | with	| with	| ADP	| 		|  | O	| 		0                 |  0 |                                               
| token_32	 | the	| the	| DET	| 	| 	| O		| 	0                  |  0 |                                                      
| token_33	 | swing	| swing	| NOUN	| wn:07066042n	| 	| O	| 0                   | 		1                                       |
| token_34	 | revival	| revival	| NOUN	| wn:01047338n	| 	|  O	| 	0	                 | 0                                   |
| token_35	 | band	| band	| NOUN	| wn:08240169n	| | 	O 	| 	0 |  1 |
| token_36	 | Squirrel	| Squirrel	| PROPN		| | ORG	| B	| Squirrel Nut Zippers	|  0 |  0 |
| token_37	 | Nut	| Nut	| PROPN		|  |  ORG	| I	| 		0 |  0 |                             
| token_38	 | Zippers	| Zippers	| PROPN	| 	| ORG	| I		| 	0 | 0 |
| token_39	 | .	| .	| PUNCT	| 	| 	| O	| 	0 | 0 |


## The Wikipedia module
It was created selecting from **[BabelNet domains](http://lcl.uniroma1.it/babeldomains/)** all the **[Wikipedia](https://www.wikipedia.org)** musical pages.

### Annotations
The annotation of the module can be downloaded from:

| lang | url     | - |
|------|---------|---|
| DE   | http:// | - |
| EN   | http:// | - |
| ES   | http:// | - |
| FR   | http:// | - |
| IT   | http:// | - |
| NL   | http:// | - |



## The Periodicals module
It was created with the help of musicologists that provided the titles of different influencial music periodicals.

### Annotations

The annotation of the module can be downloaded from:

| lang | url     | - |
|------|---------|---|
| DE   | http:// | - |
| EN   | http:// | - |
| ES   | http:// | - |
| FR   | http:// | - |
| IT   | http:// | - |
| NL   | http:// | - |



## The Polifonia Pilots module
It was created collecting the textual material selected by five **[Polifonia Pilots](https://polifonia-project.eu/pilots/)**:
- BELLS
- CHILD
- MEETUPS
- MUSICBO
- ORGANS


### Annotations

The annotation of the module can be downloaded from:

| Pilot   | url     | -   |
|---------|---------|-----|
| BELLS   | http:// | - |
| CHILD   | http:// | - |
| MEETUPS | http:// | - |
| MUSICBO | http:// | - |
| ORGANS  | http:// | - |
