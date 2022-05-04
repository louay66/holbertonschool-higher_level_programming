#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedBYdict = dict(sorted(a_dictionary.items()))
    for i, j in sortedBYdict.items():
        print(f"{i}: {j}")
