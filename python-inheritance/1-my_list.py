#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that has a method to print a sorted version of itself.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """

        print(sorted(self))
