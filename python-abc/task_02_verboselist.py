#!/usr/bin/python3
"""
Extending the Python List with Notifications
"""


class VerboseList(list):
    """A list that prints notifications on modifications."""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        count = 0
        for _ in iterable:
            count += 1
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
