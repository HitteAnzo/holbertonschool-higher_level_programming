#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size',
and includes methods for initialization and calculating the area of the square.
"""


class Square:
    """
    A class that defines a square by its size and calculates its area.
    
    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        
        Args:
            size (int): The size of the square (must be an integer >= 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
