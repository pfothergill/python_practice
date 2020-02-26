#!/usr/bin/python3

n = 101
count = 1
while count <= n:
    stars = "*" * count
    print(stars.center(n))
    count += 2