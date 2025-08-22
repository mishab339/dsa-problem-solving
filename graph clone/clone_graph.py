# solved using BFs
# time complexity = O(V+E)

from collections import deque
# Definition for a Node
class Node:
    def __init__(self,val=0):
        self.val = val
        self.neighbors = []

#clone a Graph     
def cloneGraph(node):
    if not node:
        return None

    mp = {}
    q = deque([node])
    mp[node] = Node(node.val)
    while q:
        current = q.popleft()

        for neighbor in current.neighbors:
            if neighbor not in mp:
                mp[neighbor] = Node(neighbor.val)
                q.append(neighbor)
        
            mp[current].neighbors.append(mp[neighbor])
    return mp[node]

#compare graph
def compareGraph(n1,n2,visited):
    if not n1 or not n2:
        return n1==n2
    if n1.val != n1.val or n1 is n2:
        return False
    visited[n1] = n2

    if len(n1.neighbors) != len(n2.neighbors):
        return False
    
    for i in range(len(n1.neighbors)):
        neighbor1 = n1.neighbors[i]
        neighbor2 = n2.neighbors[i]

        if neighbor1 in visited:
            if visited[neighbor1] != neighbor2:
                return False
            
        else:
            if not compareGraph(neighbor1,neighbor2,visited):
                return False
    return True
#Build graph
def BuildGraph():
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    node1.neighbors = [node2,node3]
    node2.neighbors = [node1,node3]
    node3.neighbors = [node1,node2,node3]
    node4.neighbors = [node3]
    return node1
    

original = BuildGraph()
clone = cloneGraph(original)
result = compareGraph(original,clone,{})
print("True" if result else "false")
