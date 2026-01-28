#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index without modifying
    the original list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the element to replace.
        element: The new element to insert at the specified index.

    Returns:
        A new list with the element replaced, or a copy of the original
        list if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
