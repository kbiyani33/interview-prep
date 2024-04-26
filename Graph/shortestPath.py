from typing import List, Tuple
from collections import deque
import math

class Solution:
    def dfs_topo_sort(self, V:int, adjList: List[List[Tuple[int]]], node:int, visited:List[bool], stack:deque):
        visited[node] = True
        for edge in adjList[node]:
            dst, weight = edge[0], edge[1]
            if not visited[dst]:
                self.dfs_topo_sort(V=V, adjList=adjList, node=dst, visited=visited, stack=stack)
        stack.appendleft(node)

    def shortestPathUsingDFS(self, adjList:List[List[Tuple[int]]], V:int, sourceNode:int) -> List[int]:
        # V = number of nodes and adjList is the adjList of weighted graph
        result = [math.inf]*V
        result[sourceNode] = 0

        # step 1 do a topological sort using DFS
        stack = deque()
        visited = [False]*V
        for i in range(V):
            if not visited[i]:
                self.dfs_topo_sort(V=V, adjList=adjList, visited=visited, node=i, stack=stack)
        
        # Now my stack will be toposorted
        # print(stack)
        while(len(stack) > 0):
            top = stack.popleft() # top of stack is always stack[0] don't get confused here.
            # print(top)
            for adjacent in adjList[top]:
                destination, weight = adjacent[0], adjacent[1]
                result[destination] = min(result[destination], weight + result[top])
        
        return result


    def convertEdgeToAdjacencyList(self, n:int, m:int, edges:List[List[int]]) -> List[List[Tuple[int]]]:
        adjList = [[] for i in range(n)]
        # n nodes and m vertices
        for edge in edges:
            src, dst, weight = edge[0], edge[1], edge[2]
            adjList[src].append((dst, weight))
        return adjList
    
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adjList = self.convertEdgeToAdjacencyList(n=n, m=m, edges=edges)
        shortestDistances =  self.shortestPathUsingDFS(adjList, n, sourceNode=0)
        for i in range(n):
            if shortestDistances[i] == math.inf:
                shortestDistances[i] = -1
        return shortestDistances