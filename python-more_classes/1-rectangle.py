#!/usr/bin/python3
"""creating a class"""


class Rectangle:
    """creating a class named Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """creating a getter for width"""
        return self.__width

    @property
    def height(self):
        """creating a getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """creating a setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """creating a setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
