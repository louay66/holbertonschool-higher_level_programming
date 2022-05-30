#!/usr/bin/python3
""" class  named Square tat inhert from Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is a class inhert form Rectangle
    """

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):

        return self.__size ** 2
