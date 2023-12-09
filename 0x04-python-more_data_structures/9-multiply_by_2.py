#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary

    # new_dictionary =\
    #     dict(map(lambda item: (item[0], item[1] * 2), a_dictionary.items()))
    # return new_dictionary
