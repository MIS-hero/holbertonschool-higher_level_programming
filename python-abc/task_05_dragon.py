#!/usr/bin/python3
"""
Using mixins to give Dragon the ability to swim and fly
"""


class SwimMixin:
    """Mixin providing swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly."""

    def roar(self):
        print("The dragon roars!")
