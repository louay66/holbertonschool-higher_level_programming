#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    a = 0
    for i in str:
        if i != n:
            new += str[i]
        a += 1
    return new
