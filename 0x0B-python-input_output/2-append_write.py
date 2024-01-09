#!/usr/bin/python3
"""Defines a file function."""


def append_write(filename="", text=""):
    """Appends a string .

    Args:
        filename (str): name of file
        text (str): The string
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as o:
        return o.write(text)
