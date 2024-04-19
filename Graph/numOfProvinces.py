#User function Template for python3
from typing import List
from collections import deque
class Solution:
    def dfs(self, adj:List[List[int]], starting:int, visited:List[bool]):
        if visited[starting]:
            return
        visited[starting] = True
        for i in adj[starting]:
            if not visited[i]:
                self.dfs(adj, i, visited)
    
    def bfs(self, adj:List[List[int]], starting:int, visited:List[bool]):
        q = deque()
        q.append(starting)
        while(len(q) != 0):
            element = q.popleft()
            visited[element] = True
            for i in adj[element]:
                if not visited[i]:
                    q.append(i)
        
        
    def numProvinces(self, adj, V):
        # code here
        adjLs = [[] for i in range(V)]
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
        # print(adjLs)
        visited = [False]*V
        provinces = 0
        for i in range(V):
            if not visited[i]:
                provinces += 1
                self.dfs(adjLs, i, visited)
        return provinces