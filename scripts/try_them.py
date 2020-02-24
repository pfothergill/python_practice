#!/usr/bin/python3

def foo1(x):
    return x ** 0.5

def foo2(x, y):
    if x > y:
        return x
    return y

# Test foo1()
print(foo1(4))
print(foo1(9))
print(foo1(100))

# Test foo2()
print(foo2(2, 4), 'x=2 y=4')
print(foo2(3, 1), 'x=3 y=1')
print(foo2(3, 3), 'x=3 y=3')

