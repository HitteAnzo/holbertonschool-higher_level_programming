#!/usr/bin/env python3
"""
Module task_04_flyingfish
Defines classes Fish, Bird, and FlyingFish to demonstrate multiple inheritance.
"""


class Fish:
    """
    Class representing a Fish with swimming capability and habitat information.
    """
    def swim(self):
        """
        Prints the swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a Bird with flying capability and habitat information.
    """
    def fly(self):
        """
        Prints the flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """
        Overrides fly method to describe the flying behavior of a flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Overrides swim method to describe the swimming behavior of flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Overrides the habitat method to describe
        the unique habitat of a flying fish.
        """
        print("The flying fish lives both in water and the sky!")
