#!/usr/bin/python3
def remove_char_at(str, n):
    new = str
    if n >= 0:
        new = new[:n] + new[n+1:]
    return new
