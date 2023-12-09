#!/usr/bin/python3
def common_elements(set_1, set_2):
    # list_1 = list(set_1)
    # list_2 = list(set_2)

    # new_list = []

    # for i in range(len(list_1)):
    #     for j in range(len(list_2)):
    #         if list_1[i] == list_2[j]:
    #             new_list.append(list_1[i])
    #             continue

    # return new_list

    new_set = set(map(lambda x: x if x in set_2 else None, set_1))
    new_set.discard(None)

    return new_set

    # new_set = set_1.intersection(set_2)
    # return new_set
