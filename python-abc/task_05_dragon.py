#!/usr/bin/env python3
"""
Defines mixins SwimMixin a FlyMixin,
and a class Dragon that inherits from both.
"""


class SwimMixin:
    """
    Mixin class to add swimming capability.
    """
    def swim(self):
        """
        Prints a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class to add flying capability.
    """
    def fly(self):
        """
        Prints a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can both swim and fly, using mixins.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
