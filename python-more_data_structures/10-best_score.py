#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = max(a_dictionary.values())
    return (max_score)
