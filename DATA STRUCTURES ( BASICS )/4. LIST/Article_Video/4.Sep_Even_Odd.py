"""
Input : [8, 12, 15, 9, 3, 11, 26, 23]
Output : Even lists: [8, 12, 26]
         Odd lists: [15, 9, 3, 11, 23]


Input : [2, 5, 13, 17, 51, 62, 73, 84, 95]
Output : Even lists: [2, 62, 84]
         Odd lists: [5, 13, 17, 51, 73, 95]
"""


def Even_Odd(x):
    even=[]
    odd=[]

    for i in x:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

x=list(map(int, input("Enter numbers: ").split()))
even,odd = Even_Odd(x)
print("Even list ")
print(even)
print("odd list")
print(odd)

""" ⭕ T/C- O(n) """