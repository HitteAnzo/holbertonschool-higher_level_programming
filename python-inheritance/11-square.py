#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(self, size): Initializes a square instance.
        area(self): Returns the area of the square.
        __str__(self): Returns the string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        The size is validated as a positive integer
        using the integer_validator method from BaseGeometry.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The description of the square in the format
            [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
