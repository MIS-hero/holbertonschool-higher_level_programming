#!/usr/bin/python3
"""creating a function"""


def inherits_from(obj, a_class):
    """writhing the method of the function"""
    return isinstance(obj, a_class) and type(obj) is not a_class
