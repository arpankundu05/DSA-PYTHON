# Delete Kth Node of Circular Linked List

# Function delete First node of Circular Linked List
def DeleteFirst(head):
    previous = head
    next = head

    # check list have any node if not then return
    if (head == None) :
    
        print("\nList is empty")
        return None
    
    # check list have single node if yes then delete it and return
    if (previous.next == previous) :
    
        head = None
        return None
    
    # traverse second to first
    while (previous.next != head):
        previous = previous.next
        next = previous.next
    
    # now previous is last node and next is first node of list first node(next) link address put in last node(previous) link
    previous.next = next.next

    # make second node as head node
    head = previous.next

    return head
  
# This code is contributed by shivanisinghss2110