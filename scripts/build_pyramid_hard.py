#!/usr/bin/python3

import sys

def make_pyramid(n):
    count = 1
    while count <= n:
        spaces = " " * int((n - count) / 2)
        stars = "*" * count
        print(spaces + stars + spaces)
        count += 2

def count_total_stars(n):
    count = 0
    while n >= 1:
        if n == 1:
            return count + 1
        else:
            count += n
            n -= 2
    return count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('\nUsageError: ')
        print(' '*14 + 'python3 build_pyramid_hard.py <arg1>  <--------MISSING ARGUEMENT\n')
        sys.exit(1)
    else:
        bottom_row_stars = int(sys.argv[1])
        print('\n', str(count_total_stars(bottom_row_stars)), 'total stars!' + '\n')
        make_pyramid(bottom_row_stars)
        print('\n')
