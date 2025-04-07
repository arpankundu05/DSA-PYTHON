"""
Input : arr[] = {8, 100, 20, 40, 3, 7}, x = 10
Output : {8, 3, 7}
Elements less than x are 8, 3, and 7.

Input : arr[] = {100, 20, 40, 60, 80}, x = 60
Output : {20, 40}
Elements less than x are 20 and 40.
"""

def Smaller_Elements(x,n):
    elements=[]
    for i in x:
        if i<n:
            elements.append(i)
    return elements

x=list(map(int, input("Enter numbers: ").split()))
n=int(input("Enter a number print befor all smallest element : "))
print(Smaller_Elements(x,n))

""" ⭕ T/C- O(n) """