#!/usr/bin/python3
"""My base module"""


class Base:
    """Defines a base class for unittests"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes the object

            Args:
                id (int): id of person
        """
        if id:
            self.id = id
        if not id:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
