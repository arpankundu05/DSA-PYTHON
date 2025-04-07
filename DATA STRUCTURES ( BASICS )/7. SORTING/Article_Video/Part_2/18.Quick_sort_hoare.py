# Quick Sort using Hoare's Partition


def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as the pivot
    i = low - 1
    j = high + 1

    while True:
        # Move right until we find an element greater than or equal to the pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move left until we find an element smaller than or equal to the pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If two pointers have met, return the partition index
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)  # Partition index
        quick_sort(arr, low, pi)  # Sort left subarray (Hoare returns j, not j+1)
        quick_sort(arr, pi + 1, high)  # Sort right subarray

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

"""The time complexity is O(n log n)."""