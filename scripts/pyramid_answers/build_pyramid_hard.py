#!/usr/bin/python3

# to run this script: python3 build_pyramid_hard.py <number of rows> where rows needs to be an odd number
# example: python3 build_pyramid_hard.py 5

#  9 total stars!

#    *  
#   *** 
#  *****

# importing sys allows us to work directly with the computer
import sys

# this function is the same as the one in build_pyramid_medium
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


# new function to count the number of total stars
# n == stars in bottom row
def count_total_stars(n):
    count = 0 # set a count var to equal 0
    # run a loop while stars is greater than one. Nothing is printed, however each iteration takes the count of that rows worth
    # of stars and then adds that to the total count. Afterwards, it takes off 2 stars and runs the loop again until
    # stars in a row == 1 (means it's finally to the top-most row) and returns the value of the count
    #     *     iteration 3 (n = 1, @ the end, count = 9, and 9 is returned)
    #    ***    iteration 2 (n = 3, @ the end, count = 8)
    #   *****   iteration 1 (n = 5, @ the end, count = 5)
    while n >= 1:
        if n == 1: # base case, if given an odd number in argv, this will always run which will return the count + 1 == total stars
            return count + 1
        else:
            count += n # add star count in current row to the total count
            n -= 2 # decrease stars for next row to n - 2, where n is current row's number of stars
    return count # return total stars

# as long as an argv value was given, run the functions 
# example: python3 build_pyramid_hard.py arg1 arg2 arg3 ... arg[i]
# sys.argv[0] == script name or in this case build_pyramid_hard.py
# sys.argv[1:] (here 1: means from index 1 onward) or in this case 1==arg1 2==arg2 3==arg3 i==arg[i]
# so if I had python3 build_pyramid_hard.py 9 
# sys.argv[0] == build_pyramid_hard.py
# sys.argv[1] == 9
# and there is no sys.argv[2] and onward as no more arguements are given!!!
if len(sys.argv) < 2: # sys.argv is a list so you can check that the length is less than 2 meaning the script name was given but no arguements
    # print some fancy stuff
    print('\nUsageError: ')
    print(' '*14 + 'python3 build_pyramid_hard.py <arg1>  <--------MISSING ARGUEMENT\n')
    sys.exit(1) # exit with error code 1
# if this part and below runs, it means that there were at least 2 arguements given. Hopefully only 2 but in 
# either case only the script name (sys.argv[0]) and the first arguement (sys.argv[1]) matter
else:
    bottom_row_stars = int(sys.argv[1]) # set the second item in argv list equal to the number of bottom row stars
    # find the total number of stars by calling the count_total_stars(n) function with n being equal to 
    # bottom_row_stars (which is argv[1]). Print out the number that is returned (as a string).
    print('\n', str(count_total_stars(bottom_row_stars)), 'total stars!' + '\n')
    # make the pyramid by calling the function make_pyramid(n) with n being equal to bottom_row_stars (which is argv[1]) 
    make_pyramid(bottom_row_stars)
    # the '\n' means print a newline character, which is invisible in standard output. It basically means print an empty line
    print('\n')

