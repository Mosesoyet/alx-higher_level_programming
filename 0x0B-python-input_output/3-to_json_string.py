#!/usr/bin/python3
"""
A program that returns JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """A function that serializes my_obj to a json string
    """
    return json.dumps(my_obj)
