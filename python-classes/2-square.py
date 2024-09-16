#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size',
and includes methods for initialization and validating the size.
"""


class Square:
    """
    A class that defines a square by its size.
    With validation for the size attribute.

    Attributes:
    __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the square (default is 0).

        Must be an integer and greater than or equal to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
