#!/usr/bin/python3
def no_c(my_string):
    modified_string = my_string.translate({ord(i): None for i in 'cC'})
    return modified_string
