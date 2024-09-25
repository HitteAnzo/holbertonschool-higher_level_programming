#!/usr/bin/env python3
"""
This module defines an abstract class Shape.
And concrete classes Circle Rectangle.
Includes a function to print the area and perimeter of any shape object.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape that serves as a blueprint for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute the area of the shape.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute the perimeter of the shape.
        Must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Computes the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Computes the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any shape object using duck typing.

    Args:
        shape (Shape): The shape object
        whose area and perimeter will be printed.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    return area, perimeter
    
