#!/usr/bin/python3
"""Unittest module for class `Rectangle`"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines various test cases for class `Rectangle`"""

    def test_init_with_valid_arguments(self):
        """Test init constructor with valid arguments"""
        rect = Rectangle(2, 4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertIsNotNone(rect.id)

    def test_init_with_invalid_arguments(self):
        """Test init construtor with invalid arguments"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 4)

        with self.assertRaises(TypeError):
            rect = Rectangle(2, "4")

    def test_area(self):
        """Test area mehtod"""
        rect = Rectangle(3, 5)
        self.assertEqual(rect.area(), 15)

    def test_display(self):
        rect = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rect.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test string representation """
        rect = Rectangle(2, 4, 1, 2, 99)
        expected_output = "[Rectangle] (99) 1/2 - 2/4"
        self.assertEqual(str(rect), expected_output)

    def test_update(self):
        """Test update method"""
        rect = Rectangle(2, 4, 1, 2, 99)
        rect.update(5, 3, 6, 7, 88)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 88)
