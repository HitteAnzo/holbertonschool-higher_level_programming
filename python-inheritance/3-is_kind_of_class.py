#!/usr/bin/python3
"""
This module defines a function is_kind_of_class.
The function checks if an object is an instance of a given class
or if it is an instance of a class that inherited from the given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.
    Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class or parent class to check against.

    Returns:
        True if obj is an instance or inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
