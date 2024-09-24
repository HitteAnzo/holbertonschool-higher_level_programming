#!/usr/bin/env python3
"""
This module defines a VerboseList class
that extends the built-in list class.
Notifications are printed when items are added or removed from the list.
"""


class VerboseList(list):
    """
    VerboseList is a custom list class that prints notifications
    whenever an item is added or removed from the list.
    """

    def append(self, item):
        """
        Overrides the append method to add an item to the list
        and print a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Overrides the extend method to extend the list
        and print a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Overrides the remove method to remove an item from the list
        and print a notification.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Overrides the pop method to pop an item from the list
        and print a notification.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
