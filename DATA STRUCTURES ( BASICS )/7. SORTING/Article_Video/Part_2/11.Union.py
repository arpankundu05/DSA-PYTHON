# Union of Two Sorted Arrays
"""Consider two arrays a=[1,2,4,5,6] and b=[2,4,4,6,8] then their union will be 1,2,4,5,6,8"""

def Union(a, b):
    res = []
    m = len(a)
    n = len(b)
    i = j = 0

    while i < m and j < n:
        if a[i] < b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
            
        else:  # If both are equal, add only once
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1

    while i < m:
        if not res or res[-1] != a[i]:
            res.append(a[i])
        i += 1
    while j < n:
        if not res or res[-1] != b[j]:
            res.append(b[j])
        j += 1
    return res

a = [10, 15]
b = [5, 6, 6, 30, 40]

print(*Union(a, b))

"""Time Complexity: O(m + n)"""

# Another approch
def union_of_two_sorted_array(a,b):
    i=j=0
    result=[]
    while (i<len(a) and j<len(b)):
        if (i>0 and a[i]==a[i-1]):
            i+=1
        elif (j>0 and b[j]==b[j-1]):
            j+=1
        elif (a[i]<b[j]):
            result.append(a[i])
            i+=1
        elif (a[i]>b[j]):
            result.append(b[j])
            j +=1
        else:
            result.append(a[i])
            i +=1
            j +=1
    while (i<len(a)):
        if (i>0 and a[i] != a[i-1]):
            result.append(a[i])
            a+=1
    while (j<len(b)):
        if (j>0 and b[j] != b[j-1]):
            result.append(b[j])
            j +=1
    return result

a = [10, 15]
b = [5, 6, 6, 30, 40]

print(*union_of_two_sorted_array(a, b))

"""Time Complexity: O(m + n)"""