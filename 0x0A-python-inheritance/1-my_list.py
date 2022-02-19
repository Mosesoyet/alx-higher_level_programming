#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """An attempt to create the class MyList"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
