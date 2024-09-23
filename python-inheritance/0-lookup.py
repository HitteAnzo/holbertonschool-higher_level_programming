#!/usr/bin/python3
"""
Return the list of available attributes.
"""


def lookup(obj):
    """
    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings representing the object's
    """

    return dir(obj)
