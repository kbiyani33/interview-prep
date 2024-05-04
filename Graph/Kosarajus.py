from typing import List

class Solution:
    
    def getOrderDFS(self, V:int, adj:List[List[int]], visited:List[bool], stack:List[int], node:int):
        visited[node] = True
        for adjacent in adj[node]:
            if not visited[adjacent]:
                self.getOrderDFS(V, adj, visited, stack, adjacent)
        stack.append(node)
    
    def dfs(self, V:int, adj:List[List[int]], visited:List[bool], node:int):
        visited[node] = True
        for adjacent in adj[node]:
            if not visited[adjacent]:
                self.dfs(V, adj, visited, adjacent)
    
    def getTransposeGraph(self, V:int, adj:List[List[int]]) -> List[List[int]]:
        transpose = [[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                transpose[j].append(i)
        return transpose
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V:int, adj:List[List[int]]):
        visited = [False]*V
        stack = []
        
        for i in range(V): # step 1 get the latest fill time nodes
            if not visited[i]:
                self.getOrderDFS(V, adj, visited, stack, i)
        # print(stack)
        transpose = self.getTransposeGraph(V, adj) # step 2 get the transpose of the graph by reversing the edges
        # print(transpose)
        scc = 0
        newVisited = [False]*V
        while stack:
            node = stack.pop()
            if not newVisited[node]:
                scc += 1
                self.dfs(V, transpose, newVisited, node)
        return scc