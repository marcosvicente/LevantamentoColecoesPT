#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import os


class CreateTxtClass():
    def __init__(self, file, class_names, separator, value, classes_column ):
        self.file = file
        self.class_names = class_names
        self.separator = separator
        self.value = value
        self.classes_column = classes_column


    def read_csv(self):
        file_csv = pd.read_csv(
            self.file,
            sep=str(self.separator),
            header=None,
        )
        return file_csv

    """
    if the class be positive save in path positive
    """
    def create_directory(self):
        for classes in self.class_names:
            directory = 'database/preprocess/{0}'.format(classes)
            if not os.path.exists(directory):
                os.makedirs(directory)


    def create_txt(self, data, name_class, line_number):
        self.create_directory()
        for classes in self.class_names:
            if name_class == classes:
                create = open('database/preprocess/{0}/{0}_{1}.txt'.format(classes, line_number), 'w+')
                create.write(data)
                create.close()

    def get_value_csv(self, file_csv):
        print(self.classes_column)
        for line_number in range(len(file_csv)):
            data = (file_csv.values[line_number][int(self.value)])

            name_class = (file_csv.values[line_number][int(self.classes_column)])
            self.create_txt(data, name_class, line_number)


    def main(self):
        return self.get_value_csv(self.read_csv())

