from typing import List
from collections import deque

class Solution:

    def detect_cycle_directed_graph_bfs(self, V:int, adj:List[List[int]]) -> bool :
        topoSort = []
        q = deque()
        indegree = [0] * V
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while len(q) > 0:
            node = q.popleft()
            topoSort.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return len(topoSort) < V
    
    def directed_graph_cycle_detection_dfs(self, V:int, adj:List[List[int]], visited:List[bool], pathVisited:List[bool], sourceNode:int) -> bool:
        # mark sourceNode as visited and pathVisited
        visited[sourceNode] = True
        pathVisited[sourceNode] = True

        # Now go through the neighbors of sourceNode
        for neighbor in adj[sourceNode]:
            if not visited[neighbor]:
                if self.directed_graph_cycle_detection_dfs(V=V, adj=adj, visited=visited, pathVisited=pathVisited, sourceNode=neighbor):
                    return True
            elif pathVisited[neighbor]:
                # i.e. cycle is detected and return True
                return True
        pathVisited[sourceNode] = False
        return False


    #Function to detect cycle in a directed graph.
    def isCyclic(self, V:int, adj:List[List[int]]) -> bool:
        # code here
        visited = [False]*V
        pathVisited = [False]*V

        for i in range(V):
            if not visited[i]:
                if self.directed_graph_cycle_detection_dfs(V=V, adj=adj, visited=visited, pathVisited=pathVisited, sourceNode=i):
                    return True
        
        return False