from typing import List
from collections import deque
import math

class Solution:

    def bfs_traversal_from_source(self, adjList:List[List[int]], V:int, visited:List[bool], distance:List[int], startNode:int):
        q = deque()
        q.append((startNode, 0))
        visited[startNode] = True
        distance[startNode] = 0

        while(len(q) > 0):
            node, nodeDist = q.popleft()
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    neighborDistance = min(nodeDist+1, distance[neighbor])
                    visited[neighbor] = True
                    q.append((neighbor, neighborDistance))
        

    def getAdjacencyListUndirected(self, edges:List[List[int]], n:int, m:int) -> List[List[int]]:
        adjList = [[] for i in range(n)]
        for edge in edges:
            src, dest = edge[0], edge[1]
            adjList[src].append(dest)
            adjList[dest].append(src)
        return adjList

    def shortestPath(self, edges:List[List[int]], n:int, m:int, src:int) -> List[int]:
        # n nodes and m edges
        print(edges)
        adjList = self.getAdjacencyListUndirected(edges=edges, n=n, m=m)
        print(adjList)
        distancesArray = [math.inf]*n
        visited = [False]*n

        self.bfs_traversal_from_source(adjList, V=n, visited=visited, distance=distancesArray, startNode=src)
        return distancesArray