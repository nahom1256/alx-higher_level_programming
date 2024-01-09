#!/usr/bin/python3
"""Defines a function."""
import json


def from_json_string(my_str):
    """Return the Python object"""
    return json.loads(my_str)
