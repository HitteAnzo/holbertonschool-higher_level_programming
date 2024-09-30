#!/usr/bin/python3
"""
Module that contains a function to return
a dictionary description for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serializable attribute of the object.
    """
    return obj.__dict__
