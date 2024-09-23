#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width, height): Initializes a rectangle instance.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        The width and height are validated as positive integers
        using the integer_validator method from BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
