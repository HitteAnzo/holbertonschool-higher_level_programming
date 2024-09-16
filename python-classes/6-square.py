#!/usr/bin/python3
"""
This module defines a class Square with private instance attributes 'size' and 'position',
and methods for initialization, retrieving and setting these attributes, calculating the area,
and printing the square using the '#' character.
"""


class Square:
    """
    A class that defines a square by its size and position. Allows setting and getting
    size and position, calculates the area, and prints the square using the '#' character
    with spaces based on the position.
    
    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        
        Args:
            size (int): The size of the square (default is 0). Must be an integer
            and greater than or equal to 0.
            position (tuple): The position of the square (default is (0, 0)). Must be
            a tuple of 2 positive integers.
        
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains negative values.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. Validates the type and value.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.
        
        Returns:
            tuple: The position of the square (a tuple of 2 positive integers).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute. Validates the type and value.
        
        Args:
            value (tuple): The new position of the square.
        
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character to stdout. 
        The position is indicated by spaces and new lines based on position[0] and position[1].
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Handle the vertical position by printing new lines
        for _ in range(self.__position[1]):
            print()

        # Handle the horizontal position and the square size
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
