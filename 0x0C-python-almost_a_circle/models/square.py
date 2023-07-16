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
