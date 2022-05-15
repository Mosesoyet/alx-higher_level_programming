#!/usr/bin/python3
"""
A program tha read a file content
"""


def read_file(filename=""):
    """Read a file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
