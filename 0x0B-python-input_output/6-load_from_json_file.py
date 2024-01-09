#!/usr/bin/python3
"""Defines a function."""
import json


def load_from_json_file(filename):
    """Create a Python object"""
    with open(filename) as o:
        return json.load(o)
