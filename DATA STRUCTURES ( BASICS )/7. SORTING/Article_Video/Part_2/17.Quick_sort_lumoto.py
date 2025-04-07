# Quick Sort using Lomuto Partitio

def lomuto_partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1  

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in correct position
    return i + 1  # Return pivot index

def quick_sort(arr, low, high):
    if low < high:
        pi = lomuto_partition(arr, low, high)  # Partition index
        quick_sort(arr, low, pi - 1)  # Sort left subarray
        quick_sort(arr, pi + 1, high)  # Sort right subarray

arr = [10, 7, 8, 9, 1, 5,6]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


"""The time complexity is O(n^2)."""