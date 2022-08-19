#!/usr/bin/python3
""" Search API"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    ama = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        res = ama.json()
        if res == {}:
            print("No result")
        else:
            id = res['id']
            name = res['name']
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
