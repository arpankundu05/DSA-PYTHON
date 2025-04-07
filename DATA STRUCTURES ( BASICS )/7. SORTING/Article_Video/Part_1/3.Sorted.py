# Sorted in Python

"""This built-in function, sorted() always returns a new list containing the sorted elements from an iterable (like a list, tuple, string, etc).
"""

l = [10, 20, 14]
ls = sorted(l)

print(l)
print(ls)

l = [10, -15, -2, 1]
ls = sorted(l, key=abs, reverse=True)
print(ls)
"""
Absolute values of [10, -15, -2, 1] are [10, 15, 2, 1].

Sorting in descending order gives [15, 10, 2, 1].

The actual values that correspond to this ordering are [-15, 10, -2, 1]
"""

t = (10,12,5,1)
print(sorted(t))

s = {'gfg','courses','python'}
print(sorted(s))

st = 'gfg'
print(sorted(st))

d = {10:'gfg',15:'ide',5:'courses'}
print(sorted(d))

l = [(10,15),(1,8),(2,3)]
print(sorted(l))