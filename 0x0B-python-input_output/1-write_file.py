#!/usr/bin/python3
"""
A program that writes a string into a text file\
        UTF8 format
"""


def write_file(filename="", text=""):
    """Writing the text into the file given filename
    filename: the name of the file to be written
    text: file content in text.
    """
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))
