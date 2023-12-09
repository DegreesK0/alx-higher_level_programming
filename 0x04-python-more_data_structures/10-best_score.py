#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_score = 0
    best_key = None

    for key, value in a_dictionary.items():
        if best_score < value:
            best_score = value
            best_key = key

    return best_key
