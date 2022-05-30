#!/usr/bin/python3
""" class  named Rectangle tat inhert from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a class inhert form basegeometry
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
