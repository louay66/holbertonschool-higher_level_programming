#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) >= ord('z'):
            char = chr(ord(c) - 32)
            print("{:s}".format(char), end="")
        else:
            print("{:s}".format(c), end="")
    print('')
