#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []
    for elem in my_list:
        newlist.append(elem)
    i = len(my_list) - 1
    if idx < 0:
        return newlist
    elif idx > i:
        return newlist
    else:
        newlist[idx] = element
    return newlist
