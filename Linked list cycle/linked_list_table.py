#Bruit force method using hashSet
# time complexity = O(n)
# space complexity = O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectLoop(head):
    st = set()

    while head is not None:
        if head in st:
            return True
        st.add(head)
        head = head.next
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next
print(detectLoop(head))  # Output: True

# using floyd's cycle finding algorithsm
# time complexity = O(n)
# space complexity = O(1)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def detectLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next
print(detectLoop(head))  # Output: True