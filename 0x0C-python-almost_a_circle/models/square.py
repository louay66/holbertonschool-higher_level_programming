#!/usr/bin/python3
"""As you know, a Square is a special Rectangle, so it makes sense
this class Square inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class inhert from class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):

        return self.width

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):

        return "[Square] ({}) {}/{} - {}\
                ".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):

        my_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return my_dict
