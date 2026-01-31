#!/usr/bin/python3
"""creating a class"""


class Rectangle:
    """creating a class named Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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

    def area(self):
        """creating the area"""
        return self.width * self.height

    def perimeter(self):
        """creating a perimter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """creating a print function"""
        if self.width == 0 or self.height == 0:
            new_str = ""
            return new_str
        else:
            row = str(self.print_symbol) * self.width
            row = [row] * self.height
            new_str = "\n".join(row)
            return new_str

    def __repr__(self):
        """creating a reper"""
        new = "Rectangle({}, {})".format(self.width, self.height)
        return new

    def __del__(self):
        """creating a deleting function"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
