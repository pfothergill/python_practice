#!/usr/bin/python3

def foo1(x):
    return x ** 0.5

def foo2(x, y):
    if x > y:
        return x
    return y

def foo3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    if x > y:
        tmp = y
        y = x
        x = tmp
    return [x, y, z]

def otherfoo3(x, y, z):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    if x > y:
        tmp = y
        y = x
        x = tmp
    return [x, y, z]
# Test foo1()
print(foo1(4))
print(foo1(9))
print(foo1(100))

# # Test foo2()
print(foo2(2, 4), 'x=2 y=4')
print(foo2(3, 1), 'x=3 y=1')
print(foo2(3, 3), 'x=3 y=3')

# # Test foo3()
print(foo3(1, 2, 3), otherfoo3(1, 2, 3))
print(foo3(2, 4, 1), otherfoo3(2, 4, 1))
print(foo3(4, 2, 1))
print(foo3(4, 2, 5))
print(foo3(16, 10, 13))
