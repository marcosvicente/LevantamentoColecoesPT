#!/usr/bin/env python3
# coding: utf-8

import argparse
import os
import csv
import re
import pandas as pd
import numpy as np
import nltk
import unidecode
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from operator import itemgetter

from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from string import punctuation
import multiprocessing as mp
import time

from create_txt_class import CreateTxtClass
from generate_bow import GenerateBow

class Preprocess():
    def database2csv(self, input_classes, output_path):
        data = pd.DataFrame()
        list_docs = list()
        list_classes= list()
        list_filename= list()

        classes = os.listdir(input_classes)
        for class_ in classes:
            doc_label = os.path.join(input_classes, class_)
            docs = os.listdir(doc_label)

            for doc in docs:
                doc_path = os.path.join(doc_label, doc)
                file = open(doc_path, "r", encoding="utf8")
                text = file.read().replace('\n', ' ').replace('\r', ' ')
                list_docs.append(text)
                list_classes.append(class_)
                list_filename.append(doc)
                file.close()
        data['file_name'] = list_filename
        data['classes'] = list_classes
        data['text'] = list_docs
        data.sort_values(by=['file_name'])
        return data


    def text2lower(self, text):
        return text.lower()

    tokenizer = RegexpTokenizer(r'\w+')
    def tokenize(self, text):
        return word_tokenize(text)

    def remove_numbers(self, text):
        return [re.sub("\d+","", ch) for ch in text]

    def clean(self, tokens):
        result = []
        for token in tokens:
            if (len(token) > 1):
                result.append(unidecode.unidecode(str(token)))
        return result

    """
    remove punctuation such as ! ? etc
    """
    def replace_punct(self, text):
        text_without_punctuation = " "

        sentences = sent_tokenize(text)
        for s in sentences:
            text_tokens = self.tokenize(s)
            for w in text_tokens:
                for punct in punctuation:
                    w = w.replace(punct," ")
                if w != " ":
                    text_without_punctuation = text_without_punctuation + " " + w
            text_without_punctuation = text_without_punctuation + " ."
        return text_without_punctuation + " "

    # fazendo comportamento diferente ver
    def remove_stopwords(self, tokens):
        if stopwords_file != None:
            file = open(stopwords_file, "r")
            s = file.read().replace("\n", " ")
            stopset = s.split()
        else:
            stopset = stopwords.words('portuguese')

        return [t for t in tokens if t not in stopset]

    def stem(self, tokens):
        stemmer = SnowballStemmer(language)
        result = []
        for token in tokens:
            result.append(stemmer.stem(token))
            # print(result)
        return ' '.join(result)


    def create_path(self, output_dir):
        if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        if not os.path.exists(output_dir + "representations"):
                os.makedirs(output_dir + "representations")


    def run(self):
        self.create_path(output_dir)
        print('> Create a txt')

        df = CreateTxtClass(file, classes_name, separator, value_csv, classes_column).main()

        print('> Loading data files')
        df = self.database2csv(input_dir, output_dir)
        print('> Done')


        print("> Preprocessing TXT files to BOW")
        df['bow_preproc'] = df['text'].apply(self.text2lower).apply(self.replace_punct).apply(self.tokenize).apply(self.clean).apply(self.remove_numbers).apply(self.remove_stopwords).apply(self.stem)
       
        print('\t> Done')


        print("> INICIO DAS REPRESENTACOES")
        # Gerador filenames
        bow_tf_output_file = "bow_tf_" + database + ".csv"
        bow_tfidf_output_file = "bow_tfidf_" + database + ".csv"
        preprocess_output_file = "preprocess_" + database + ".csv"

        print('\t> Generating BOW - TF')
        GenerateBow(df, output_dir, bow_tf_output_file).generate_bow_tf()
        print('\t> Done BOW - TF')

        print('\t> Generating BOW - TFidf')
        GenerateBow(df, output_dir, bow_tfidf_output_file).generate_bow_tfidf()
        print('\t> Done BOW - TFidf')

        print('\t> Done')

        df.to_csv(os.path.join(output_dir, preprocess_output_file), sep="|", index=None)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert TXT documents to a labeled CSV file.'
    )
    parser.add_argument(
        '-i',
        '--input_dir',
        required=True,
        help='Input data directory.'
    )
    parser.add_argument(
        '-o',
        '--output_dir' ,
        required=True, help='Output data directory.'
    )
    parser.add_argument(
        '-l',
        '--language',
        required=False,
        help='Language used in files.'
    )

    parser.add_argument(
        '-d',
        '--database',
        required=True,
        help='Database name.'
    )
    parser.add_argument(
        '-f',
        '--file',
        required=False,
        help='File name.'
    )
    parser.add_argument(
        '-sw',
        '--stopwords',
        required=False,
        help='Stopwords list file.'
    )
    parser.add_argument(
        '-cl',
        '--classes',
        nargs='+',
        required=True,
        help='Class list file.'
    )

    parser.add_argument(
        '-cc',
        '--classes-column',
        required=False,
        help='Class column in file.'
    )
    parser.add_argument(
        '-sp',
        '--separator',
        required=False,
        help='Separator list file.'
    )
    parser.add_argument(
        '-vl',
        '--value',
        required=False,
        help='Column of value'
    )


    args = parser.parse_args()


    input_dir = args.input_dir

    output_dir = args.output_dir

    stopwords_file = args.stopwords

    classes_name = args.classes

    classes_column = args.classes_column

    separator = args.separator

    value_csv = args.value

    language = args.language

    database = args.database.lower()

    file = args.file

    procs = mp.cpu_count()-1

    Preprocess().run()



