#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary:
        count = 0
        for key, value in a_dictionary.item():
            count += 1
        return count
