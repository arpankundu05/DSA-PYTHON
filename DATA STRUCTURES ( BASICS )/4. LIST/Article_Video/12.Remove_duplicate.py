# Remove Duplicates
"""
I/P: [2, 2, 2, 2, 2]
O/P: 1

I/P: [1, 2, 2, 3, 4, 4, 4, 5, 5]
O/P: 5
"""

# Efficincy approch
def remove_duplicate(arr,n):
    count=0
    new_arr=[]
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
            count +=1
    return count
        
arr=list(map(int, input("Enter numbers: ").split()))
n=int(input("Size of array: "))
print(remove_duplicate(arr,n))

""" ⭕ T/C- O(n) """

# Swapping method
def remove_duplicate(arr,n):
    res=1
    for i in range(1,n):
        if (arr[res-1] != arr[i]):
            arr[res]=arr[i]
            res +=1
    return res
        
arr=list(map(int, input("Enter numbers: ").split()))
n=int(input("Size of array: "))
print(remove_duplicate(arr,n))

""" ⭕ T/C- O(n) """