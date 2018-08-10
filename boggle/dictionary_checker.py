"""This module is concerned with creating sets from dictionaries"""

DICTIONARY_PATH = '../dictionary.txt'


def set_from_file(file_path):
    "Returns a set containing all words in `file_path`"
    word_set = set()

    with open(file_path, 'r') as words_file:
        for line in words_file:
            word_set.add(line.rstrip('\n'))  # removes line breaks

    return word_set
