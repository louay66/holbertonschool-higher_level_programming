#!/usr/bin/python3
""" POST request to the passed URL with the email as a parameter"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    data_encoding = parse.urlencode(data).encode()
    reqest = request.Request(argv[1], data_encoding, method='POST')
    with request.urlopen(reqest) as response:
        print(response.read().decode('utf-8'))
