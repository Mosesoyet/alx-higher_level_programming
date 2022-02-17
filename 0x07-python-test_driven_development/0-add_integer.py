#!/usr/bin/python3
"""
A program that adds two integers
"""

def add_integer(a, b=98):
    """A function that add integer"""
    if type(a) is not int or type(a) is not float:
        """Checks for type of a"""
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        """checks b"""
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
