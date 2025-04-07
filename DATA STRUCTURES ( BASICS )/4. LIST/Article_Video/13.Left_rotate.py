# Left Rotate a list by one
"""
I/P: [10,20,30,40]
O/P: [20,30,40,10]

I/P: [1,2,3,4]
O/P: [2,3,4,1]
"""

# Rotate a list using Slicing 
def left_rotate(x):
    l=x[1:]+x[0:1]
    return l

x=list(map(int, input("Enter numbers: ").split()))
print(left_rotate(x))

""" ⭕ T/C- """

# Append/Pop
def left_rotate(l):
    temp=l.pop(0)
    l.append(temp)
    return l

x=list(map(int, input("Enter numbers: ").split()))
print(left_rotate(x))

""" ⭕ T/C- """

#  Iterative Method
def left_rotate(l):
    n=len(l)
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
    return l

x=list(map(int, input("Enter numbers: ").split()))
print(left_rotate(x))

""" ⭕ T/C- """