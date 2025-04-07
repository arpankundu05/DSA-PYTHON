# Check is a list is Sorted

"""
Input : 20 21 45 89 89 90
Output : Yes

Input : 20 20 45 89 89 90
Output : Yes

Input : 20 20 78 98 99 97
Output : No
"""

# Built in function
def isSorted(l):
    l2 = sorted(l)
    if l==l2:
        return True
    else:
        return False
  
l = [10,20,30,15,40]
if isSorted(l):
    print("Yes")
else:
    print("No")
    
# Iterative approach:
def isSorted(l):
    i = 1
    while i< len(l):
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True
    
l = [10,20,30,15,40]
if isSorted(l):
    print("Yes")
else:
    print("No")
    
""" ⭕ T/C- O(n) """