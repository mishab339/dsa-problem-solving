# using DFS
# Time complexity = O(V + E)
# space complexity = O(V)

def validTree(n,edges):
    if not n:
        return True
    adj = {i:[] for i in range(n)}

    for n1,n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    visited = set()
    def dfs(i,prev):
        if i in visited:
            return False
        visited.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j,i):
                return False
        return True
    return dfs(0,-1) and len(visited) == n

n = 5 
edges = [[0,1],[0,2],[0,3],[1,4],[4,0]]   

import datetime
start = datetime.datetime.now()
print(validTree(n,edges))
end = datetime.datetime.now()
print(end - start)
    