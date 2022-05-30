#!/usr/bin/python3
""" class  named BaseGeometry
"""


class BaseGeometry:
    """this is a class
    """

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError(name+" must be an integer")
        if value <= 0:
            raise ValueError(name+ " must be greater than 0")

    def area(self):

        raise Exception("area() is not implemented")
