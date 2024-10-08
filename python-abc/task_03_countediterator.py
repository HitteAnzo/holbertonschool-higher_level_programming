#!/usr/bin/env python3
"""
Module task_03_countediterator
Defines a class CountedIterator that extends
the functionality of an iterator
by keeping track of how many items have been iterated over.
"""


class CountedIterator:
    """
    A class that wraps around an iterable
    And counts the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with the iterable and a counter.

        Args:
            iterable (iterable): The iterable object to wrap around.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: If there are no more items in the iterator.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Returns the number of items that have been iterated over.

        Returns:
            int: The count of items iterated.
        """
        return self.count
