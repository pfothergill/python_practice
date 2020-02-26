#!/usr/bin/python3

import sys

num_of_stars = int(sys.argv[1])

def make_pyramid(n):
    count = 1
    while count <= n:
        spaces = " " * int((n - count) / 2)
        stars = "*" * count
        print(spaces + stars + spaces)
        count += 2

if __name__ == '__main__':
    make_pyramid(num_of_stars)
