#!/usr/bin/python3
"""Defines a function."""


def write_file(filename="", text=""):
    """Write a string

    Args:
        filename (str): name of file 
        text (str): text in the file 

    """
    with open(filename, "w", encoding="utf-8") as o:
        return o.write(text)
