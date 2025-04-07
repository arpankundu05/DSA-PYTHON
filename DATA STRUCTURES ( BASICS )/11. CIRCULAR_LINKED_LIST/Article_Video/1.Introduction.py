# Introduction to Circular Linked List
"""
A circular linked list is a special type of linked list where all the nodes are connected to form a circle. Unlike a regular linked list, which ends with a node pointing to NULL, the last node in a circular linked list points back to the first node. This means that you can keep traversing the list without ever reaching a NULL value.
"""

# Advantages and Disadvantages of Circular Linked List

# Advantages of Circular Linked Lists:
"""
→ It is possible to traverse from the last node back to the first i.e. the head node.
→ The starting node does not matter as we can traverse each and every node despite whatever node we keep as the starting node.
→ The previous node can be easily identified.
→ There is no need for a NULL function to code. The circular list never identifies a NULL identifier unless it is fully assigned.
→ Circular linked lists are beneficial for end operations as start and finish coincide. 
Algorithms such as Round Robin setup can effectively complete online queues without having to meet NULL suspension or reference checks.
"""

# Disadvantages of Circular Linked Lists:
"""
→ If the circular linked list is not handled properly then it can lead to an infinite loop as it is circular in nature.
→ In comparison with singly-linked lists, doubly linked lists are more complex in nature
→ Direct accessing of elements is not possible.
→ It is generally a complex task to reverse a circular linked list.
"""