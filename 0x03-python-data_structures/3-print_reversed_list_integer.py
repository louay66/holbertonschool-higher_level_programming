#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        newlist = my_list[::-1]
        print(*newlist, sep='\n')
