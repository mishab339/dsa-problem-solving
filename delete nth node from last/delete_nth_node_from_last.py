#using the length of list
#time complexity = O(n)
#space complexity = O(1)

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

def deleteNthNodeFromEnd(head,n):
    k = 0
    curr = head
    while curr:
        curr = curr.next
        k += 1

    if k - n == 0:
        return head.next
    
    curr = head
    for _ in range(1,k - n):
        print("one")
        curr = curr.next
    
    curr.next = curr.next.next
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = deleteNthNodeFromEnd(head,4)

curr = head
while curr:
    print("data: ",curr.data)
    curr = curr.next

#using fast and slow pointer
#time complexity = O(n)
#space complexity = O(1)

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None


def deleteNthNodeFromEnd(head,n):
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    
    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = deleteNthNodeFromEnd(head,4)
curr = head
while curr:
    print(curr.data)
    curr = curr.next

