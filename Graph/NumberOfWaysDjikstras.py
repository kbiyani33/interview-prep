from typing import List
from collections import defaultdict, deque
import heapq, math, sys

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        MODULO = 1000000007
        
        # create adj list
        adjList = [[] for i in range(n)]
        for road in roads:
            u,v,t = road[0], road[1], road[2]
            adjList[u].append([v,t])
            adjList[v].append([u,t])
        
        times = [math.inf] * n
        ways = [0] * n
        
        times[0], ways[0] = 0,1 # src = 0
        heap = []
        heapq.heappush(heap, (0, 0))
        
        while len(heap) > 0:
            t, n = heapq.heappop(heap)
            for ad in adjList[n]:
                dest, time = ad[0], ad[1]
                totalTime = t + time
                if totalTime < times[dest]:
                    times[dest] = totalTime
                    ways[dest] = ways[n]
                    heapq.heappush(heap, (totalTime, dest))
                elif totalTime == times[dest]:
                    ways[dest] += ways[n]
        
        return ways[-1]