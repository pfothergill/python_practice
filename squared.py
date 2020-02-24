#!/usr/bin/python3

def squared(start=1, end=10):
    # create an empty list to catch results during each iteration
    results = []
    for i in range(start, end):
        r = i * i # could also do i ** 2 where ** means exponent kind of like i^2 (** == ^)
        # append results to results list
        results.append(r)
    # return the results list
    return results

print(squared())
print(squared(0, 10))
print(squared(2,20))