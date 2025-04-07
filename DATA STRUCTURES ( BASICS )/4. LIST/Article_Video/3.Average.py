"""
Given a list of numbers, the task is to find average of that list. Average is the sum of elements divided by the number of elements.

Input : [4, 5, 1, 2, 9, 7, 10, 8]
Output : Average of the list = 5.75

Input : [15, 9, 55, 41, 35, 20, 62, 49]
Output : Average of the list = 35.75
"""

# Using built in module-
def average(x):
    return sum(x)/len(x)

x=list(map(int, input("Enter numbers: ").split()))
print(average(x))

""" ⭕ T/C- O(n) """

# Using iterating list--
def average(x):
    sum=0
    count=0
    for i in x:
        sum = sum+i
        count = count+1
    avg = sum/count
    return avg
    
x=list(map(int, input("Enter numbers: ").split()))
print(average(x))

""" ⭕ T/C- O(n) """