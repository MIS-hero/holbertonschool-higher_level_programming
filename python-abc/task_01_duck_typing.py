#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """Return the area of the shape."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the shape."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the shape."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the shape."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape-like object (duck typing)."""
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
        return area, perimeter
    except Exception:
        pass
