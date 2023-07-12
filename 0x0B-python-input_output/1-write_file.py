#!/usr/bin/python3
"""This module defines a file writing function"""


def write_file(filename="", text=""):
    """
        Writes texts to a file

        Args:
            filename (string): name of the file to be written to
            text (string): text to write to the file

        Returns: the number of characters writtten
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
