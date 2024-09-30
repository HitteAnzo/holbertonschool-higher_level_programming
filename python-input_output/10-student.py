#!/usr/bin/python3
"""
Module that defines a Student class with attributes
and a method to return a dictionary representation.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with the given
        First name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts a Student object to a dictionary.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of
            the Student object for JSON serialization.
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict
