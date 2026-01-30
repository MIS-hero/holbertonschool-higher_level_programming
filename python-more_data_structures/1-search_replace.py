#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for item in my_list:
        if item == search:
            Index = my_list.index(search)
            my_list[Index] = replace
    return my_list
