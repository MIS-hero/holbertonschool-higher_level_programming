#!/usr/bin/python3
"""
This module defines the User class and related helper functions
for managing user information in the application.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size):
        '''
        Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.
        '''
        self.__size = size
