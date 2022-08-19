#!/usr/bin/python3
"""my status"""
import requests
from sys import argv

if __name__ == "__main__":
    ama = requests.get(argv[1])
    print(ama.headers.get("X-Request-Id"))
