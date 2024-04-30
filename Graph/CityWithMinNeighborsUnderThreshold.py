"""
There are n cities labeled from 0 to n-1 with m edges connecting them. 
Given the array edges where edges[i] = [fromi , toi ,weighti]  represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold. 
You need to find out a city with the smallest number of cities that are reachable through some path and whose distance is at most Threshold Distance. 
If there are multiple such cities, our answer will be the city with the greatest label.

Note: The distance of a path connecting cities i and j is equal to the sum of the edge's weights along that path.
"""

# Can be solved using Floyd Warshal and djikstras. We will solve using both.


from typing import List
import math, heapq

class Solution:
    def djikstras(self, V:int, adjList:List[List[List[int]]], src:int) -> List[int]: # this function is needed to return an array of minimum distances from a src to all V vertices
        distances = [math.inf]*V
        distances[src] = 0
        heap = []
        heapq.heappush(heap, (0, src))
        while heap:
            dist, node = heapq.heappop(heap)
            for neighbor in adjList[node]:
                dest, weight = neighbor[0], neighbor[1]
                totalDist = dist + weight
                if distances[dest] > totalDist:
                    distances[dest] = totalDist
                    heapq.heappush(heap, (totalDist, dest))
        return distances
    
    def djikstras_solution(self, n:int, m:int, edges:List[List[int]], distanceThreshold:int) -> int: # this only works because all distances are positive
        adjList = [[] for i in range(n)]
        for edge in edges:
            src, dest, weight = edge[0], edge[1], edge[2]
            # bidirectional so both sides will be updated
            adjList[src].append([dest, weight])
            adjList[dest].append([src, weight])
        
        distances = [[] for i in range(n)]
        for i in range(n):
            # make i to be the source and get the distances array for all the other nodes
            distances[i] = self.djikstras(V=n, adjList=adjList, src=i)
        # print(distances)
        countCity = n+1
        city = -1
        for i in range(n):
            counti = 0
            for j in range(n):
                if distances[i][j] <= distanceThreshold:
                    counti += 1
            if countCity >= counti:
                countCity = counti
                city = i
        return city
    
    def floydWarshalAlgorithm(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        adjMatrix = [[math.inf]*n for i in range(n)]
        for edge in edges:
            u,v,w = edge[0], edge[1], edge[2]
            adjMatrix[u][v] = w
            adjMatrix[v][u] = w
        
        # initialization
        for i in range(n):
            adjMatrix[i][i] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][via]+adjMatrix[via][j])
        
        countOfCities = n+1
        toReturn = -1
        # print(adjMatrix)
        for i in range(n):
            countI = 0
            for j in range(n):
                if adjMatrix[i][j] <= distanceThreshold:
                    countI += 1
            if countI <= countOfCities:
                countOfCities = countI
                toReturn = i
        return toReturn

    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        # code here
        return self.djikstras_solution(n,m,edges, distanceThreshold)
                    


