# Bubble Sort

# Using for loop
def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]> l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

l=[58,10,5,20,8,1,9,15]
print(*l)
bubblesort(l)
print(*l)

# Using while loop
def bubbleSort(l):
    n = len(l)
    i = 0  # Outer loop counter
    while i < n - 1:
        j = 0  # Inner loop counter
        while j < n - i - 1:
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
            j += 1  
        i += 1  

l=[58,10,5,20,8,1,9,15]
bubbleSort(l)
print("\n",*l)

"""Time Complexity: O(n^2)
Space Complexity: O(1)"""