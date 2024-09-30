#!/usr/bin/python3

"""
This module defines a `Student` class that provides methods
for serializing and deserializing student attributes to and from JSON.
"""


class Student:
    """
    A class used to represent a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If `attrs` is provided, only the attributes listed in `attrs`
        will be included in the returned dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include.
            If not provided, all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict

    def reload_from_json(self, json):
        """
        Replaces the attributes
        Student instance with the values from `json`.

        Args:
            json (dict): A dictionary where keys correspond to attribute names
            and values to the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
