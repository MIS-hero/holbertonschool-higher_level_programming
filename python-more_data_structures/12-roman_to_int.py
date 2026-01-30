#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for char in roman_string:
        if (char == 'V' or char == 'X') and total % 5 == 1:
            total += roman_numerals[char] - 2
        elif (char == 'L' or char == 'C') and total % 50 == 10:
            total += roman_numerals[char] - 20
        elif (char == 'D' or char == 'M') and total % 500 == 100:
            total += roman_numerals[char] - 200
        else:
            total += roman_numerals[char]
    return total
