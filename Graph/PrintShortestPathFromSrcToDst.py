# User function Template for python3
# User function Template for python3
from typing import List
import math, heapq
from collections import deque


class Solution:
    def convertToAdjacencyList(
        self, n: int, m: int, edges: List[List[int]]
    ) -> List[List[List[int]]]:
        adj = [[] for i in range(n + 1)]  # since n vertices are 1 indexed
        for i in range(m):  # since m edges
            edge = edges[i]
            node1, node2, wt = edge[0], edge[1], edge[2]
            adj[node1].append([node2, wt])
            adj[node2].append([node1, wt])
        return adj

    def shortestPath(self, n: int, m: int, edges: List[List[List[int]]]) -> List[int]:
        # first convert the edges to adjacency list
        adjList = self.convertToAdjacencyList(n, m, edges)
        # print(adjList)
        # now we will apply a small djikstras algorithm on this adj list

        # take a distance array and a parent array of size n=vertices
        parent = [-1] * (n + 1)
        distance = [math.inf] * (n + 1)
        distance[1] = 0
        # print(distance)
        # print(parent)

        # source is 1 and destination is n

        heap = []
        heapq.heappush(
            heap, (0, 1)
        )  # 0 distance to reach node 1 and no parent updation

        while len(heap) > 0:
            distanceSoFar, node = heapq.heappop(heap)
            # print(distanceSoFar)
            # print(node)
            # print(adjList[node])
            # now move to neighbors of node
            for neighbor in adjList[node]:
                near, distanceToNeighbor = neighbor[0], neighbor[1]
                totalPathDistance = distanceSoFar + distanceToNeighbor
                # print(near)
                # print(distanceToNeighbor)
                # print(totalPathDistance)
                if totalPathDistance < distance[near]:
                    parent[near] = node
                    distance[near] = totalPathDistance
                    heapq.heappush(heap, (totalPathDistance, near))

        # print(distance)
        # print(parent)
        if distance[n] == math.inf:
            return [-1]
        path = []
        node = n
        while parent[node] != -1:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()
        # print(path)
        return [distance[n]] + path
