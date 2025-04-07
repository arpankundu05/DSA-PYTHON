# Second Largest Element in a List

"""
I/P: [12, 35, 1, 10, 34, 1]
O/P: 34

I/P: [10, 5, 10]
O/P: 5

I/P: [10, 10, 10]
O/P: 10
"""

# Efficint approch
def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]; slar = None
    for x in l[1:]:
        if x > lar:         # if current element is greater than lar(largest element)
            slar = lar          # update slar to largest
            lar = x         # update lar to current element(largest)
        elif x != lar:      # if x is less then largest and not equal to lar(largest element)
            if slar == None or slar < x:    # if x is greater then second largest
                slar = x                    # assign current element is second largest
    return slar
l = [int(x) for x in input().split()]
print(getSecMax(l))

""" ⭕ T/C- O(n) """


# Another solution 
def getMax(l):
    if not l:
        return None
    else:
        res = l[0]                  # assume l[0] is the max
        for i in range(1, len(l)):  # iterate through index 1 to last
            if l[i] > res:           # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
        return res
def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    slar = None
    for x in l:
        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(x, slar)
    return slar
l = [int(x) for x in input().split()]
print(getSecMax(l))