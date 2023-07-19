#!/usr/bin/python3
"""Unittes  module for class `Square`"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines various test cases for the class Square"""

    def test_init_with_valid_arguments(self):
        """Test init constructor with valid arguments"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_init_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            square = Square(-5)
        with self.assertRaises(TypeError):
            square = Square("5")

    def test_area(self):
        """Test area method"""
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_display(self):
        """Test display method"""
        square = Square(2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            square.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        square = Square(4, 1, 2, 99)
        expected_output = "[Square] (99) 1/2 - 4"
        self.assertEqual(str(square), expected_output)


    def test_update(self):
        square = Square(4, 1, 2, 99)
        square.update(5, 3, 7, 88)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 88)
