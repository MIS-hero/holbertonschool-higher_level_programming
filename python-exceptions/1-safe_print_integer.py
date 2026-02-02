#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (any): The value to be printed.

    Returns:
        bool: True if value is an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
