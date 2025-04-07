# Comprehensions in Python
"""
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined. Python supports the following 4 types of comprehensions:

● List Comprehensions
● Set Comprehensions
● Dictionary Comprehensions
● Generator Comprehensions
"""

# List Comprehensions:

"""
List Comprehensions provide an elegant way to create new lists. The following is the basic structure of a list comprehension:
🔵 Note that list comprehension may or may not contain an if condition. List comprehensions can contain multiple for (nested list comprehensions).
"""

l = [1, 2, 3, 4, 5]

l1 = [x for x in l if x % 2 == 0]
print(l1)  # Output: [2, 4]

l2 = [x for x in l if x % 2 != 0]
print(l2)  # Output: [1, 3, 5]

# Using List comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]


list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
list_using_comp)

# Set Comprehensions:
"""
Set comprehensions are pretty similar to list comprehensions. The only difference between them is that set comprehensions use curly brackets { }. Let’s look at the following example to understand set comprehensions.
"""

l = {10,20,3,4,10,20,7,3}
s1 = {x for x in l if x%2==0 }
s2 = {x for x in l if x%2!=0 }  
print(s1)
print(s2)

# Using Set comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",set_using_comp)
# Dictionary Comprehensions:
"""
Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. The basic structure of a dictionary comprehension looks like below.
"""

l1 = [1,3,4,2,5]

d1 = {x:x**3 for x in l1}

d2 = {x:f"ID{x}" for x in range(5)} 
print(d2)


l2 = [101,103,102]
l3 = ['gfg','ide','corse']

d3 = {l2[i]:l3[i] for i in range(len(l2)) }  

print(d3)


d4 = dict(zip(l2,l3))

print(d4)

# Using Dictionary comprehensions

input_list = [1,2,3,4,5,6,7]

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",dict_using_comp)

d1 = {101:'gfg',103:'practice',102:'ide'}
d2 = {v:k for (k,v) in d1.items() }

print(d2)



# Generator Comprehensions:
"""Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets. The major difference between them is that generators don’t allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient."""

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')