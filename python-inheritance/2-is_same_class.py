#!/usr/bin/python3
"""
Defines a function is_same_class that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return (type(obj) is a_class)
