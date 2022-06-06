#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""
import json
from os import path


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if type(id) is not int and id is not None:
            raise TypeError("id must be an interger")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):

        with open(cls.__name__ + ".json", mode='w') as file_to_write:

            if list_objs is None:
                file_to_write.write("[]")
            else:
                file_to_write.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        res = []
        if path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", mode="r") as read_file:
                text = cls.from_json_string(read_file.read())

            for i in text:
                res.append(cls.create(**i))
        return res
