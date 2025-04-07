# Sorting in Python

"""
sorted()

sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending order or in descending order(does unicode comparison for string char by char) and always returns the a sorted list. This method doesn’t effect the original sequence.

Syntax: sorted(iteraable, key, reverse=False)
Parameters: 
Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted. 
Key(optional): A function that would serve as a key or a basis of sort comparison. 
Reverse(optional): If set True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
Return Type: Returns a sorted list. 
"""
# Example :-
num = [ 6, 5, 2, 3, 1 ]
sortedNum = sorted( num )
print( sortedNum )

# Time Complexity: O(n log(n))
# Space Complexity: O(n)
"""
sort()
sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. Moreover, sort() is a method of list class and can only be used with lists.

Syntax: List_name.sort(key, reverse=False)
Parameters: 
key: A function that serves as a key for the sort comparison. 
reverse: If true, the list is sorted in descending order.
Return type: None 
"""

# Example :- 
num = [ 6, 5, 2, 3, 1 ]
num.sort()
print( num )

# Time Complexity: O(n log(n))
# Space Complexity: O(1)

"""SUMMERY"""
# sort() (In-Place Sorting)

# It is a method available for lists.
# Modifies the original list and does not return a new list.
# Returns None.

# sorted() (Returns a New List)

# It is a built-in function that works on any iterable (lists, tuples, strings, dictionaries, etc.).
# Returns a new sorted list without modifying the original.
# Can be used with any iterable.