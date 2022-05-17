# Interrogation Functionalities of Polifonia Textual Corpus

The interrogation of the corpus takes advantage of the annotation described in the *[annotations](https://github.com/polifonia-project/Polifonia-Corpus/tree/master/annotations)* section of this repository.

The main script to use to interrogate the corpus is:

> interrogate.py

It has different parameters that can be used to select, navigate and store sentences of the corpus that satisfy aspecific query.
The parameters are explained below their use is described in the following sections.

1. --annotations_path: indicates the path were the annotations databases are stored (the default value is annotation/db/)
2. --download_annotations: if set to 'Yes' it download the annotations databases and place then in --annotation_path
3. --corpus: indicates what module of the corpus has to be queried. It can be Wikipedia, Books, Periodicals or Pilots
4. --lang: indicates the language to use for the interrogations. It can be DE, EN, ES, FR, IT or NL
5. --interrogation_type: indicates the type of interrogation that has to be conducted. It can be Keyword, concept or entity. Each interrogation type will be explained in the next sections.
6. --query: the keyword to use for the interrogation, e.g., guitar.
7. --sent_n: indicates the number of sentences to get at each interrogation.
8. --save_to_file: indicates if the results of the interrogations have to be saved to a file. The default value of this parameter is 'No'.

# How to use this repository

The first step is to clone the repository

> git clone https://github.com/polifonia-project/Polifonia-Corpus.git
> cd Polifonia-Corpus

The second step involves the download of the required packages

> pip install -r requirements.txt

Once the environment is set up, it is possible to test the script using the default parameters with:

> python interrogation/interrogate.py

To change the default keyword, the --query parameter has to be passed to the script:

> python interrogation/interrogation.py --query swing

In this way the word 'swing' will be searched trought the corpus and some sentences will be displayed.


## Keyword search

#### API

#### Example

## Con  cept search

#### API

#### Example

## Entity search

#### API

#### Example