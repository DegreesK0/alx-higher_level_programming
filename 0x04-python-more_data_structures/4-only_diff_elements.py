#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # new_set = set(map(lambda x: x if x not in set_2 else None, set_1))
    # new_set.update(set(map(lambda x: x if x not in set_1 else None, set_2)))
    # new_set.discard(None)

    # return new_set

    # new_set = set()

    # # Add elements from set_1 that are not in set_2
    # new_set.update(x for x in set_1 if x not in set_2)

    # # Add elements from set_2 that are not in set_1
    # new_set.update(x for x in set_2 if x not in set_1)

    # return new_set

    return set_1 ^ set_2
