#!/usr/bin/python3
"""
A program that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """A function that decode JSON file"""
    with open(filename) as f:
        return (json.load(f))
