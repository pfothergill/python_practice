#!/usr/bin/python3

# run this script by: python3 -i build_pyramid_medium_v1.py
# the -i stands for interactive
# when you run the above command you will be greated by a python3 prompt ">>>"
# type in make_pyramid(n); sustitute an odd, not even, number for n
# this number will be the amount of stars on the bottom row of the pyramid
# you can keep trying numbers and building pyramids by calling the make_pyramid(n) function, again.
# use CTRL + D to quit python3 prompt and go back to BASH prompt ( or type quit() )
def make_pyramid(n):
    count = 1 # this number is equal to the number of stars that will be printed
    
    # this loop will run for as many times as needed in order for stars to reach (but not surpass) the
    # number of stars specified by n, which is the max stars allowed in one row (in other words, stars in the bottom row)
    # In the bottom row, there will not be any extra spaces. In other words, the bottom row is all stars
    # all other rows need spaces on either side of the stars equal to the empty spaces needed to center
    # the stars. There will only be an odd number of stars on every row [1, 3, 5, 7, ...... so on]
    # now, iterate (n+1) number of times (n+1 as to count n because remember that range(n) is everything up to but not including n)
    for row in range(n + 1):
        # remember that stars will only be printed in medium amounts, so we can iterate n number of times
        # only printing some stars if row is an odd number
        # first iteration through, row = 1 and conditional runs
        # second iteration through, row = 2 and conditinal (row % 2 == 1) is False so..
        # third iteration through, row = 3 and conditional runs, sets stars = "***" and spaces = "   " <-- 3 spaces
        if row % 2 == 1:
            # make stars equal to the row number
            stars = "*" * row
            # spaces are figured by the number of spaces left in a row after stars are made with equal amounts on both sides
            # so for 3 stars in the row and 9 total spaces, 9 total spaces - 3 stars = 6 spaces left over. Use
            # 3 spaces on either side of the stars in order to center the row!
            spaces = " " * int((n - row) / 2)
            # print out the row
            print(spaces + str(stars) + spaces)
