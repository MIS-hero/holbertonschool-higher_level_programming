#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""imports the library"""


class Animal(ABC):
    """creating a class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """creating another class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """creating creating a class"""
    def sound(self):
        return "Meow"
