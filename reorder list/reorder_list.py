#time complexity = O(n)
#space complexity = O(1)
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def printList(node):
    if node is None:
        return 
    while node is not None:
        print(node.val, end=" ")
        node = node.next

def reversList(node):
    prev = None
    curr = node
    next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    node = prev
    return node

def rearrange(node):
    slow = node
    fast = slow.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    node1 = node
    node2 = slow.next
    slow.next = None

    node2 = reversList(node2)
    node = Node(0)
    curr = node
    
    while node1 is not None or node2 is not None:
        if node1 is not None:
            curr.next = node1
            curr = curr.next
            node1 = node1.next
        if node2 is not None:
            curr.next = node2
            curr = curr.next
            node2 = node2.next
    return node.next
            
head = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head = rearrange(head)
printList(head)
    