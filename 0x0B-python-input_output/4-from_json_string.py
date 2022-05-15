#!/usr/bin/python3
"""
A program that decode json string
"""
import json


def from_json_string(my_string):
    """Function that returns string from json file"""
    return json.load(my_string)
