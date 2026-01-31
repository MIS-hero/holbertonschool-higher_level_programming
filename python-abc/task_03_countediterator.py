#!/usr/bin/python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """
        Fetch next item from the iterator,
        increment count, and return the item.
        """
        item = next(self.iterator)  # raises StopIteration automatically
        self.count += 1
        return item

    def get_count(self):
        """Return number of items iterated so far."""
        return self.count
