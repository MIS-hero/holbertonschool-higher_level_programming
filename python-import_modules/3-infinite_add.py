#!/usr/bin/python3
import sys
if __name__ == "__main__":
    number = len(sys.argv)
    value = 0
    for i in range(1, number):
        value = value + int(sys.argv[i])
    print(value)
