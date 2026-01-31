#!/usr/bin/python3
"""module that contains function"""


class MyList(list):
    """creating a class called MyList"""
    def print_sorted(self):
        """function that print the list after sorting it"""
        print(sorted(self))
