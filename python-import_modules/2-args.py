#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("{} argument:".format(number))
        print("{}: {}".format(number, sys.argv[number]))
    else:
        print("{} arguments:".format(number))
        for i in range(1, number + 1):
            print("{}: {}".format(i, sys.argv[i]))
