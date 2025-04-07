# Reverse a list in Python
"""
I/P: [10, 20, 30]
O/P: [30, 20, 10]
"""

# Using Python Libraries which are as follows:

# Without creating new list
def reverse_list(l):
    l.reverse()  # reverse the list in place, modifying the original list
    return l

x=list(map(int, input("Enter numbers: ").split()))
print(reverse_list(x))

""" ⭕ T/C- O(n) """

# Creating new list
def reverse_list(l):
    new_l = list(reversed(l))  # create a new list by reversing the original list
    return new_l

x=list(map(int, input("Enter numbers: ").split()))
print(reverse_list(x))

""" ⭕ T/C- O(n) """

# Slicing method
def reverse_list(l):
    new_l = l[::-1]  # create a new list by reversing the original list using slicing
    return new_l

x=list(map(int, input("Enter numbers: ").split()))
print(reverse_list(x))

""" ⭕ T/C- O(n) """

# Using append function
def reverse_list(l):
    r_list = []
    for i in range(len(l) - 1, -1, -1):
        r_list.append(l[i])
    return r_list

x=list(map(int, input("Enter numbers: ").split()))
print(reverse_list(x))

""" ⭕ T/C- O(n) """

# Using two pointer approach
def reverse_list(l):
    s = 0
    e = len(l) - 1

    while s < e:
        l[s], l[e] = l[e], l[s]  # swapping left element to right and right element to left
        s = s + 1
        e = e - 1
    return l

x=list(map(int, input("Enter numbers: ").split()))
print(reverse_list(x))

""" ⭕ T/C- O(n) """