#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gets size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints the square in # """

        if self.__size == 0:
            print()

        for row in range(self.__size):
            for col in range(self.__size):
                if col != self.__size:
                    print("#", end="")
            print()
