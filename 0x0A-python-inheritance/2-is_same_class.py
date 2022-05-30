#!/usr/bin/python3
""" module 2-is_same_class.py
returns True if the object is exactly an instance of
the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """that check if the classes is same
    or not"""

    return True if type(obj) is a_class else False
