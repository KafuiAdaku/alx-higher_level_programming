#!/usr/bin/python3
"""My base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string representation of list_dictionaries

            Args:
                list_dictionaries (lsit): a list of dictionaries

            returns: a json string
        """
        if list_dictionaries == None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
             writes the JSON string representation of list_objs to a file

             Args:
                cls (class): class of object
                list_objs (list):  list of instances that inherit from Base
        """
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs is None:
            with open(filename,'w', encoding='utf-8') as f:
                pass

        if list_objs is not None:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation json_string

            Args:
                json_string (string): a string of list of dictionaries
        """
        return json.loads(json_string)

