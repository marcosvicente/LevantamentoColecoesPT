#!/usr/bin/env python3
# coding: utf-8

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd


class GenerateBow():
    def __init__(self, df, output_dir, output_file):
        self.df = df
        self.output_dir = output_dir
        self.output_file = output_file

    def save_file(self, lines, columns, output, bow):
        for l in range(0,lines):

            output.write(str(self.df['classes'][l]))
            output.write(str(';'))
            for c in range(0,columns):
                output.write(str(bow[l,c]))
                if c != columns-1:
                    output.write(";")
                else:
                    output.write("\n")


    def generate_bow_tf(self):
        count_vect = CountVectorizer()
        bow_tf_count_vector = count_vect.fit_transform(self.df['bow_preproc'])

        with open(os.path.join(self.output_dir,"representations", self.output_file), 'w') as output:
            list_features = count_vect.get_feature_names()

            output.write("class")
            output.write(";")
            for feature in list_features:
                output.write(feature)
                #output.write(self.df['classes'])
                if list_features.index(feature) != len(list_features)-1:
                    output.write(";")
                else:
                    output.write("\n")
s
            lines, columns = bow_tf_count_vector.shape
            self.save_file(lines, columns, output, bow_tf_count_vector)


    def generate_bow_tfidf(self):
        count_vect = CountVectorizer()
        bow_tfidf_count_vector = count_vect.fit_transform(self.df['bow_preproc'])
        tfidf_transformer = TfidfTransformer(norm=None)

        bow_tfidf = tfidf_transformer.fit_transform(bow_tfidf_count_vector)

        with open(os.path.join(self.output_dir,"representations", self.output_file), 'w') as output:
            list_features = count_vect.get_feature_names()
            output.write("class")
            output.write(";")

            for feature in list_features:
                output.write(feature)
                if list_features.index(feature) != len(list_features)-1:
                    output.write(";")
                else:
                    output.write("\n")

            lines, columns = bow_tfidf.shape
            self.save_file(lines, columns, output, bow_tfidf)



