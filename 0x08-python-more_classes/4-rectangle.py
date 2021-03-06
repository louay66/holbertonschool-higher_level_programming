#!/usr/bin/python3
"""class named rectangle
"""


class Rectangle:
    """ class Rectangle
    """
    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    def __str__(self):
        """ print the rectangle with the character #
        """
        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        for i in range(self.__height):
            for i in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """should return a string representation of
        the rectangle to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
