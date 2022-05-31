#!/usr/bin/python3
""" function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """ function that writes a string and
    returns the number of characters written"""

    with open(filename, encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
