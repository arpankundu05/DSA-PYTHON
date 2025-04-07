# One Odd Occurring
"""
Input : arr = [1, 2, 3, 2, 3, 1, 3]
Output : 3

Input : arr = [5, 7, 2, 7, 5, 2, 5]
Output : 5
"""

def findodd(arr) :
    narr=arr
    for i in narr:
        if i%2==0:
            narr.remove(i)

arr = [1, 2, 3, 2, 3, 1, 3]
print(findodd(arr))

"""
def findodd(arr) :
    res = 0 
    for i in arr :
        res = res ^ i 
    return res
if __name__ == "__main__" :
    arr = [4,3,4,4,4,5,5,3,3]
    print(findodd(arr))
    

"""