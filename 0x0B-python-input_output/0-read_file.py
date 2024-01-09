#!/usr/bin/python3
"""text"""


def read_file(filename=""):
    """Print the contents """
    with open(filename, encoding="utf-8") as o:
        print(o.read(), end="")
