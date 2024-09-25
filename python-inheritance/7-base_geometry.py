#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class BaseGeometry with public instance methods area & integer_validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the parameter (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
