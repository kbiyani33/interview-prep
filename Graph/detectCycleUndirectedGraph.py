from typing import List
from collections import deque
class Solution:
    def dfs_cycle_detection(self, V:int, adj:List[List[int]], source:int, parent:int, visited:List[bool]) -> bool:
        visited[source] = True
        for neighbor in adj[source]:
            if not visited[neighbor]:
                if self.dfs_cycle_detection(V, adj, neighbor, source, visited):
                    return True
            else:
                if parent != neighbor:
                    return True
        return False
    def bfs_cycle_detection(self, V:int, adj:List[List[int]], source:int, visited:List[bool]):
        visited[source] = True
        q = deque()
        q.append((source ,-1))
        
        while(len(q) > 0):
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, node))
                elif visited[neighbor] and parent!=neighbor:
                    return True
        return False
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		# because the graph may be broken into multiple components we will need to change the cycle
        visited = [False]*V
        for i in range(V):
            if not visited[i] and self.bfs_cycle_detection(V, adj, i, visited):
                return True
        return False