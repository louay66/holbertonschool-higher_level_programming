#!/usr/bin/python3
""" My GitHub with API"""
import requests
from sys import argv

if __name__ == "__main__":
    ama = requests.get("https://api.github.com/user",
                       auth=(argv[1], argv[2]))
    res = ama.json()
    try:
        print(res['id'])
    except KeyError:
        print(None)
