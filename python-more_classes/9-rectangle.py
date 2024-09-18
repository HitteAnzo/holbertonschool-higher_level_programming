#!/usr/bin/python3
"""
This module defines a class Rectangle with width and height attributes,
and methods to calculate area, perimeter, represent the rectangle
as a string using a customizable symbol, a repr() for object recreation,
and prints a message when an instance is deleted. It also tracks
the number of instances created and deleted, allows changing the
print symbol used for the rectangle's string representation, and
includes a static method to compare rectangles and a class method to
create a square (a rectangle with equal width and height).
"""


class Rectangle:
    """
    This class defines a rectangle by its width and height.
    It also tracks the number of instances of the class and
    allows customizing the print symbol.

    Attributes:
        number_of_instances (int): Number of instances of the class.
        print_symbol: Symbol used for string representation of the rectangle.
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0): Initializes the rectangle.
        width(self): Retrieves the width of the rectangle.
        width(self, value): Sets the width of the rectangle.
        height(self): Retrieves the height of the rectangle.
        height(self, value): Sets the height of the rectangle.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle
            using the character stored in print_symbol.
        __repr__(self): Returns a string representation that can recreate
            a new instance of the rectangle.
        __del__(self): Prints message when an instance of Rectangle is deleted.
        bigger_or_equal(rect_1, rect_2): Returns the biggest rectangle based
            on the area, or rect_1 if they are equal.
        square(cls, size): Returns a new Rectangle instance with width and
            height equal to size.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle with optional width and height.
        Increments the number_of_instances class attribute.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, ensuring it is an integer and >= 0.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle, ensuring it is an integer and >= 0.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        If width or height is 0, returns 0.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the
        character(s) stored in print_symbol.
        If width or height is 0, returns an empty string.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate
        a new instance using eval().

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles based on their area and returns the bigger one.
        If the areas are equal, returns rect_1.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater area, or rect_1 if they
            have the same area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance where width and height are equal.

        Args:
            size (int): The size of the square's sides.

        Returns:
            Rectangle: A new instance of Rectangle
            with width and height equal to size.
        """
        return cls(size, size)
