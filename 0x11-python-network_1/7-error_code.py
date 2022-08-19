#!/usr/bin/python3
""" Error code"""
import requests
from sys import argv

if __name__ == "__main__":
    ama = requests.get(argv[1])
    if ama.status_code >= 400:
        print("Error code: {}".format(ama.status_code))
    else:
        print(ama.text)
