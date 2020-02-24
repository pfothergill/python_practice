#!/usr/bin/python3

# This squares all numbers from start -> end
# By default start=1 and can be changed by calling the function with a different start number
# By default end=10 and this can also be changed by calling the function with a different end number
# squared() will use default numbers
# squared(5) will use range 5-10
# squared needs a start number if you plan on changing end number ex: squared(,5) is NOT possible. Use squared(1,5) instead
def squared(start=1, end=10): 
    # create an empty list to catch results during each iteration
    results = []
    for i in range(start, end):
        r = i * i # could also do i ** 2 where ** means exponent kind of like i^2 (** == ^)
        # append results to results list
        results.append(r)
    # return the results list
    return results

print(squared()) # arguements are optional. If not used, start=1 & end=10 by default
print(squared(0, 10))
print(squared(2, 20))
print(squared(5)) # same as squared(5,10)
