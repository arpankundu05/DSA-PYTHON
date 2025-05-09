# Insert at the Beginning of Circular Linked List

# O(N) time complexity;
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertBeg(head, x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next

    curr.next = temp
    temp.next = head
    return temp


def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(20)
head.next = Node(30)
head.next.next = head
printCircular(head)

head = insertBeg(head, 10)

printCircular(head)

# Constant time complexity:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def insertBeg(head,x):

    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        
        head.data,temp.data = temp.data,head.data   # swapping data
        return head

def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print()


head = Node(20)
head.next = Node(30)
head.next.next = head
printCircular(head)

head = insertBeg(head, 10)

printCircular(head)