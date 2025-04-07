# Merge Subarrays
"""We are given two sorted arrays. We need to merge these two arrays such that the initial numbers (after complete sorting) are in the first array and the remaining numbers are in the second array."""

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


a = [10, 15, 20, 40, 8, 11, 55]

merge(a, 0, 3, 6)

print(*a)
"""Time Complexity: O(n)
Space Complexity: O(n)"""

# Another approch

def sub_marge(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    res=[]
    m=len(left)
    n=len(right)
    i=j=0
    while i<m and j<n:
        if left[i] < right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j +=1
    while i<m:
        res.append(left[i])
        i +=1
    while j<n:
        res.append(right[j])
        j +=1
    return res

a = [10, 15, 20, 40, 8, 11, 55]

print(*sub_marge(a, 0, 3, 6))
"""Time Complexity: O(m + n)"""