from typing import List
import heapq
import math

"""
djikstra using min heap where each element is a tuple with distance and node number.
"""


class Solution:
    def djikstra_using_set(
        self, V: int, adj: List[List[List[int]]], S: int
    ) -> List[int]:
        distance = [math.inf] * V
        distance[S] = 0

        s = set()

        s.add((0, S))

        while len(s) > 0:
            distanceSoFar, node = s.pop()
            for neighbor in adj[node]:
                dest, weight = neighbor[0], neighbor[1]
                totalPathWeight = distanceSoFar + weight
                if totalPathWeight < distance[dest]:
                    if distance[dest] != math.inf and (distance[dest], dest) in s:
                        s.remove((distance[dest], dest))
                    s.add((totalPathWeight, dest))
                    distance[dest] = totalPathWeight
        return distance

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        # code here
        distance = [math.inf] * V
        distance[S] = 0
        heap = []
        heapq.heappush(heap, (0, S))

        while len(heap) > 0:
            distanceSoFar, node = heapq.heappop(heap)

            for adjacent in adj[node]:
                neighbor, distanceToNeighbor = adjacent[0], adjacent[1]
                distanceThroughNode = distanceSoFar + distanceToNeighbor
                if distance[neighbor] > distanceThroughNode:
                    distance[neighbor] = distanceThroughNode
                    heapq.heappush(heap, (distanceThroughNode, neighbor))

        return distance
