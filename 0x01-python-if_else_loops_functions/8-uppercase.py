#!/usr/bin/python3
def uppercase(str):
    newstr = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) >= ord('z'):
            newstr += chr(ord(c) - 32)
        else
            newstr += c
    print(newstr)
