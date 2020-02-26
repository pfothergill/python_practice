#!/usr/bin/python3

n = 3 # n is the number of rows in the pyramid. Change this line to get more rows!

# iterate as many times as specified by n (1 iteration == 1 row so if n = 3 then there will be 3 iterations)
# i will start at 0 and then start the loop
for i in range(n):
    # this will print out the number of stars. i is incremented by 1 because the first time through
    # i == 0 but we want 1 star, not 0. The second time through, i == 1 and we want 2 stars, not 1. So on and so forth.
    print("*" * (i + 1))