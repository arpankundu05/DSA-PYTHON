# Hoare's Partition

def hoarePartition(arr,l,h):
    pivot=arr[l]
    i=l-1
    j=h+l
    while True:
        i=i+1
        while arr[i]<pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
    # return arr

arr = [10, 80, 30, 90, 50, 70]

hoarePartition(arr, 0, 5)

print(*arr)

"""The time complexity is O(n)."""