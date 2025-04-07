# That is a naive solution 
def partition(arr,p):
    res=[]
    res.append(p)
    for i in arr[:-1]:
        if i<=p:
            res.insert(0,i)
        else:
            res.append(i)
    return res


l=[3,8,6,12,10,7,7]
print(l)
p=l[-1]
print(partition(l,p))

"""T/C- O(N^2)"""

# This is more efficincy solution than before
def partition_2(arr,p):
    left=[]
    right=[]
    right.append(p)
    for i in arr[:-1]:
        if i <= p:
            left.append(i)
        else:
            right.append(i)
    return left+right

l=[3,8,6,12,10,7,7]
print("\n",l)
p=l[-1]
print(partition(l,p))

"""T/C- O(N)"""

"""
There is more efficincy solution than this that approch are given next part.
"""