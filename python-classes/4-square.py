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
        """Initialize a Square with size validation."""
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
