#!/usr/bin/python3
for first_digit in range(10):
    for sec_digit in range(10):
        if first_digit == sec_digit:
            continue
        if first_digit > sec_digit:
            continue
        if first_digit == 8 and sec_digit == 9:
            print("{}{}".format(first_digit, sec_digit))
        else:
            print("{}{}".format(first_digit, sec_digit), end=", ")
