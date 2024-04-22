from typing import List
from collections import deque

class Solution:
    def isCyclic(self, V:int, adj:List[List[int]]) -> List[int] :
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        topoSort = []
        while(len(q) > 0):
            node = q.popleft()
            topoSort.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return topoSort

    def findOrder(self,N:int,P:int,prerequisites:List[List[int]]):
        #code here
        adj = [[] for i in range(N)]
        for i in prerequisites:
            first, second = i[1], i[0]
            adj[first].append(second)
        
        return self.isCyclic(V=N, adj=adj)