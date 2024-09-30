#!/usr/bin/python3
"""
Module that contains a function to append a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8).
    Returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The string to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
