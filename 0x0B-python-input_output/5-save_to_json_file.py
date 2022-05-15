#!/usr/bin/python3
"""
A program that saves an object to a json string
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that saves object to json string
    """
    with open(filename, "w") as fh:
        return (json.dump(my_obj, fh))
