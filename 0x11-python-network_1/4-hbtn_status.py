#!/usr/bin/python3
"""my status"""
import requests

ama = requests.get('https://intranet.hbtn.io/status')
html = ama.text
print("Body response:")
print("\t- type:", type(html))
print("\t- content:", html)
