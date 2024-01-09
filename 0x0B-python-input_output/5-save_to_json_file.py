#!/usr/bin/python3
"""Defines a function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object"""
    with open(filename, "w") as o:
        json.dump(my_obj, o)i
