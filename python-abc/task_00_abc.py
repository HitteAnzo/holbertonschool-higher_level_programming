#!/usr/bin/env python3
"""
This module defines an abstract class Animal and two subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal that defines a blueprint for derived classes.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
