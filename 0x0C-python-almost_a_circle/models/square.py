#!/usr/bin/python3
"""My Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class that inherits from a rectangle parent class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes a square instance

            Args:
                size (int) : size of the square
                x (int): horizontal coordinate
                y (int): vertical coodinate
                id (int): identity number
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            Returns a string representation of a Rectangle instance. Ex:
            [Square] (id) <x>/<y> - <width>/<height>
        """
        string = "[{}] ({}) {}/{} - {}/{}"
        cls_nm = self.__class__.__name__
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return string.format(cls_nm, self.id, x, y, width, height)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Retuens the size of the square"""
        self.width = self.integer_validator("size", value)
        self.height = self.integer_validator("size", value)

    def update(self, *args, **kwargs):
        """Assigns to attributes using *args and **kwargs"""
        attrs = ["id", "size", "x", "y"]
        if type(args) == tuple and args:
            for index, arg in enumerate(args):
                setattr(self, attrs[index], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
