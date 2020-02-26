#!/usr/bin/python3


# run this script by: python3 -i build_pyramid_medium.py
# the -i stands for interactive
# when you run the above command you will be greated by a python3 prompt ">>>"
# type in make_pyramid(n); sustitute an odd, not even, number for n
# this number will be the amount of stars on the bottom row of the pyramid
# you can keep trying numbers and building pyramids by calling the make_pyramid(n) function, again.
# use CTRL + D to quit python3 prompt and go back to BASH prompt ( or type quit() )
def make_pyramid(n):
    count = 1
    while count <= n:
        spaces = " " * int((n - count) / 2)
        stars = "*" * count
        print(spaces + stars + spaces)
        count += 2