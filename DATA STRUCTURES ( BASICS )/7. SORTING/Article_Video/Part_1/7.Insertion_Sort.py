# Insertion Sort in Python

def insertionSort(l):
    for i in range(1,len(l)):
        x = l[i]
        j = i-1
        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x
l = [20, 5, 40, 60, 10, 30]
print(*l)
insertionSort(l)
print(*l)

"""Time Complexity: O(n^2)"""