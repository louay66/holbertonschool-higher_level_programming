#!/usr/bin/python3
def uppercase(str):
    newstr = ''
    for c in str:
        if ord(c) in range(97,122):
            newstr += chr(ord(c) - 32)
        else:
            newstr += c
    print(newstr)
