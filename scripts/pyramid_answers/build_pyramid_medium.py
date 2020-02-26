#!/usr/bin/python3


# run this script by: python3 -i build_pyramid_medium.py
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
    # In the bottom row, there will not be any extra space. In other words, the bottom row is all stars
    # all other rows need spaces on either side of the stars equal to the empty spaces needed to center
    # the stars
    while count <= n:
        # spaces are generated on either side of the stars in the current row
        # spaces are 
        spaces = " " * int((n - count) / 2) # determines spaces on either side of the stars
        stars = "*" * count # determines stars in the row
        print(spaces + stars + spaces) # surround stars by equal number of spaces so all total chars in every row == n
        count += 2 # The += is shorthand for count = count + <something>, in this case, increment by 2