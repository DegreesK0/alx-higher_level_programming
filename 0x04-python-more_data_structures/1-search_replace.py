#!/usr/bin/python3
def search_replace(my_list, search, replace):

    # new_list = my_list.copy()

    # for i in range(len(new_list)):
    #     if new_list[i] == search:
    #         new_list[i] = replace

    # new_list = list(map(lambda x: replace if x == search else x, my_list))

    # return new_list

    return [replace if x == search else x for x in my_list]

    return [condition with anynoynmous variable list] with ternary

ternary has 3 operators
unary has 1 operators
