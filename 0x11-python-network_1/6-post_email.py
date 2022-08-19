#!/usr/bin/python3
"""POST an email"""
import requests
from sys import argv

if __name__ == "__main__":
    ama = requests.post(argv[1], data={'email': argv[2]})
    print(ama.text)
