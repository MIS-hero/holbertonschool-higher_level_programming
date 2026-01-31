#!/usr/bin/python3
"""creating a module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creating a class"""
    def __init__(self, size):
        """creating a function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """creating an area"""
        return self.__size * self.__size

    def __str__(self):
        """creating a way to return a string"""
        return f"[Square] {self.__size}/{self.__size}"
