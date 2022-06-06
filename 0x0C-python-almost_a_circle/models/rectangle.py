#!/usr/bin/python3
"""Rectangle module
This module defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    this is the class for rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_value_w_h(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_value_w_h(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.check_value_w_h(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.check_value_w_h(value, "y")
        self.__y = value

    def check_value_w_h(self, value, name):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0 and name in ('x', 'y'):
            raise ValueError(f"{name} must be >= 0")
        if value <= 0 and name in ("height", "width"):
            raise ValueError(f"{name} must be > 0")

    def area(self):
        return self.__height * self.__width

    def display(self):
        for space in range(self.__y):
            print("")
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print("")

    def update(self, *args, **kwargs):
        argc = len(args)
        kwargc = len(kwargs)
        my_list = ["id", "width", "height", "x", "y"]
        if argc > 0:
            if argc > len(my_list):
                argc = len(my_list)
            for i in range(argc):
                setattr(self, my_list[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in my_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "width": self.width, "height":
                self.height, "x": self.x, "y": self.y}
