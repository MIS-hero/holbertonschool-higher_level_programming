#!/usr/bin/python3
"""creating a module"""


class BaseGeometry:
    """creating a class called BaseGeometry"""
    def area(self):
        """creating a method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """creating a function"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
