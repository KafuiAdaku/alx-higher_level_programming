#!/usr/bin/python3
"""My rectangle module that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangular class which inherits from superclass Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the rectangle with it's dimensions

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int): horizontal coordinate
                y (int): vertical coordinate
        """
        Base.__init__(self, id)
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
        self.__x = self.integer_validator("x", x)
        self.__y = self.integer_validator("y", y)

    def integer_validator(self, name, value):
        """
            Validates that value is an integer >= 0

            Args:
                name (string): name of the parameter
                value (int): value of the parameter

            Returns: the value if no error is raised
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return value

    @property
    def width(self):
        """Gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width

            Args:
                value (int): width of rectangle
        """
        self.__width = self.integer_validator("width", value)

    @property
    def height(self):
        """Gets the value of the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Sets the height of the rectangle

            Args:
                value (int): height of the rectangle
        """
        self.__height = self.integer_validator("height", value)

    @property
    def x(self):
        """Gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
            Sets the value of x

            Args:
                value (int): value of x
        """
        self.__x = self.integer_validator("x", value)

    @property
    def y(self):
        """Gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
            Sets the value of y

            Args:
                value (int): the value of y
        """
        self.__y = self.integer_validator("y", value)

    def area(self):
        """Returns the area of the value of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
