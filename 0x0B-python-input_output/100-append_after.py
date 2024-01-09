#!/usr/bin/python3
"""Defines a function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename : The name of the file.
        search_string : The string to search 
        new_string : The string to insert.
    """
    ext = ""
    with open(filename) as t:
        for line in t:
            ext += line
            if search_string in line:
                ext += new_string
    with open(filename, "i") as i:
        i.write(ext)
