# Intersection of two sorted arrays
"""
Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output : Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output : Intersection : {6}
"""

def intersection(a,b):
    i=j=0
    m=len(a)
    n=len(b)
    res=[]
    while i<m and j<n:
        if a[i]==b[j]:
            if not res or res[-1]!=a[i]:
                res.append(a[i])
                i +=1
                j +=1
        elif a[i] > b[j]:
            j +=1
        elif b[j] > a[i]:
            i +=1
    
    return res

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print(*intersection(arr1,arr2))

"""Time Complexity: O(m+n)
Auxiliary Space: O(m+n)"""

# Same code with smallest approch
def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
arr1 = [1, 2, 4, 5, 5,6]
arr2 = [2, 2,3, 5, 7]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)

"""Time Complexity: O(m+n)
Auxiliary Space: O(m+n)"""