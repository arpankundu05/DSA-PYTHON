"""
Input : list1 = [10, 20, 4]
Output : 20
Input : list2 = [20, 10, 20, 4, 100]
Output : 100
"""

#  Without using built-in functions in python:
def largest_element(l):
    if not l:
        return None
    else:
        temp=l[0]
        for i in range(1,len(l)):
            if l[i] > temp:
                temp=l[i]
        return temp

x=list(map(int, input("Enter numbers: ").split()))
print(largest_element(x))

""" ⭕ T/C- O(n) """

# Naive solution(Not efficient)
def getMax(l):
    for x in l:        
        for y in l:  
            if y > x:
                break
        else:          
            return x
    return None

l = [int(x) for x in input().split()]
print(getMax(l))

""" ⭕ T/C- O(n^2) """