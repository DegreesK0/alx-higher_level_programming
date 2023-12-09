#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = dict(sorted(a_dictionary.items()))

    for key, value in list(sorted_dictionary.items()):
        print("{}: {}".format(key, value))
