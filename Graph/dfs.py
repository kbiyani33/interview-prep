from typing import List
class Solution:
    def dfs(self, adj:List[List[int]], starting:int, visited:List[bool], dfs:List[int]):
        if visited[starting]:
            return
        visited[starting] = True
        dfs.append(starting)
        neighbors = adj[starting]
        for i in neighbors:
            if not visited[i]:
                self.dfs(adj, i, visited, dfs)
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        starting = 0
        dfs_result = []
        visited = [False] * V
        self.dfs(adj, starting, visited, dfs_result)
        return dfs_result