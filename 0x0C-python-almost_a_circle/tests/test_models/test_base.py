#!/usr/bin/python3
"""Test module for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Outline various test cases for class `Base`"""

    def test_init_with_id(self):
        """Tests constructor with id"""
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        """Test constructor without id"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_init_with_invalid_id(self):
        """Test constructor with an invalid id"""
        obj = Base("invalid_id")
        self.assertRaises(TypeError, Base("invalid_id"))

    def test_to_json_string(self):
        """Test for json serialization"""
        obj1 = Base(1)
        obj2 = Base(2)
        with self.assertRaises(AttributeError):
            Base.to_json_string([obj1.to_dictionary(), obj2.to_dictionary()])

    def test_from_json_string(self):
        """Test for deserialization of json"""
        json_string = '[{"id": 1}, {"id": 2}]'
        expected_str = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.from_json_string(json_string), expected_str)
 
    def test_save_to_file(self):
        """Test saving serialized object to a file"""
        obj1 = Base(1)
        obj2 = Base(2)
        with self.assertRaises(AttributeError):
            Base.save_to_file([obj1, obj2])
