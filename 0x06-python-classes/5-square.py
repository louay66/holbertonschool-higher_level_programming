#!/usr/bin/python3
import sys
"""This is a square
"""


class Square:
    """Square Class
        """

    def __init__(self, size=0):

        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__siz == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
