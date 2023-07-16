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
        super().__init__(id)
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
        """
            that prints in stdout the Rectangle instance with the character #
        """
        breadth = 0
        for row in range(self.__height):
            for col in range(self.__width + self.__x):
                while breadth < self.__y:
                    print()
                    breadth += 1
                if col < self.__x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of a Rectangle instance. Ex:
        [Rectangle] (id) <x>/<y> - <width>/<height>
        """
        string = "[{}] ({}) {}/{} - {}/{}"
        cls_nm = self.__class__.__name__
        x = self.__x
        y = self.__y
        width = self.__width
        return string.format(cls_nm, self.id, x, y, width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attrs = ["id", "width", "height", "x", "y"]
        if isinstance(args, tuple) and args:
            for index, value in enumerate(args):
                setattr(self, attrs[index], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle instance"""
        obj_dict = {
                "id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y
                }
        return obj_dict
