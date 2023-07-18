#!/usr/bin/python3
"""My base module"""
import json
import os
import csv


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
        if list_dictionaries is None or not list_dictionaries:
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
            with open(filename, 'w', encoding='utf-8') as f:
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
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set

            Args:
                dictionary (dict): key word arguments

            Returns:
                object: Instance with attributes set based on the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_list_instances = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                inst_json = f.read()

            inst_list = cls.from_json_string(inst_json)
            for instance in inst_list:
                create_inst = cls.create(**instance)
                my_list_instances.append(create_inst)
        return my_list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes a list of objects to CSV
            
            Args:
                list_objs (list): a list of python objects
        """
        if not list_objs:
            return
        filename = cls.__name__ + ".csv"
        attributes = list_objs[0].to_dictionary().keys()
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(attributes)
            for obj in list_objs:
               writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """
            Deserializes objects from a CSV file and returns a list of
            objects
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        obj_list = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                attributes = {k: cls.convert_attribute_value(v)
                        for k, v in zip(header, row)}
                obj = cls(**attributes)
                obj_list.append(obj)
        return obj_list

    @staticmethod
    def convert_attribute_value(value):
        """
            Converts attribute value to correct data type

            Args:
                value (string): Attribute value as a string

            Returns:
                Attribute value of integer type
        """
        return int(value)
