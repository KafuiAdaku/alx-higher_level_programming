#!/usr/bin/python3
"""
This module contains a function that indents texts
"""


def text_indentation(text):
    '''This function prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    Raises:
        TypeError: If text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ctr = 0
    while ctr < len(text) and text[ctr] == " ":
        ctr = ctr + 1

    while ctr < len(text):
        print(text[ctr], end="")
        if text[ctr] == "\n" or text[ctr] in ".?:":
            if text[ctr] in ".?:":
                print("\n")
            ctr = ctr + 1
            while ctr < len(text) and text[ctr] == " ":
                ctr = ctr + 1
            continue
        ctr = ctr + 1
