#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()

    for num in my_list:
        uniq_int.add(num)

    return sum(uniq_int)
