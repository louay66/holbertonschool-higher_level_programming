#!/usr/bin/python3
"""i function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """ json file"""

    with open(filename, mode="r", encoding="utf-8") as f:

        return json.loads(f.read())
