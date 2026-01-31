#!/usr/bin/python3
"""
This module defines the User class and related helper functions
for managing user information in the application.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        '''
        Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides. Default is 0.
        '''
        self.__size = size

    @property
    def size(self):
        '''
        Get the size of the square.

        Returns:
            int: The size of the square's sides.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
