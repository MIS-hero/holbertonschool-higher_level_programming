#!/usr/bin/python3
number = 0
for i in range(122, 96, -1):
    if (122 - i) % 2 == 0:
        number = i
    else:
        number = i - 32
    print("{}".format(chr(number)), end="")
