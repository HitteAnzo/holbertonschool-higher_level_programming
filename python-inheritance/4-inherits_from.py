#!/usr/bin/python3
"""
This module defines a function inherits_from.
The function checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherits from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
