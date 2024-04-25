from typing import List
from collections import deque

class Solution:
    def bfs_topological_sort(self, V:int, adj:List[List[int]]) -> List[int]:
        topoSortedList = []
        q = deque()
        indegree = [0] * V
        visited = [False] * V
        for i in range(V):
            for j in range(adj[i]):
                indegree[j] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = True
        
        while len(q) > 0:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
                        visited[neighbor] = True
            topoSortedList.append(node)
        return topoSortedList
 
    def dfs_topological_sort(self, V:int, adj:List[List[int]], node:int, visited:List[bool], stack:deque):
        # first mark the node as visited
        if visited[node]:
            return
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs_topological_sort(V=V, adj=adj, node=neighbor, visited=visited, stack=stack)
        stack.appendleft(node) # appendleft since we want to put this element on top of the stack.
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V:int, adj:List[List[int]]) -> List[int]:
        # Code here
        stack = deque()
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                self.dfs_topological_sort(V=V, adj=adj, node=i, visited=visited, stack=stack)
        
        # print(list(stack))
        return list(stack)

