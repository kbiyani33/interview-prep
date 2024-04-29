#User function Template for python3
from typing import List
import heapq, math
from collections import deque

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        costs = [math.inf]*n
        adjList = [[] for i in range(n)]
        for path in flights:
            s,d,c = path[0], path[1], path[2]
            adjList[s].append([d, c])
            # adjList[dest].append([src, cost])
        
        # print(adjList)
        costs[src] = 0
        heap = deque()
        heap.append((0,src,0))
        while(len(heap) > 0):
            c, node, ksofar = heap.popleft()
            # traverse adjList of node
            for near in adjList[node]:
                dest, costToNode = near[0], near[1]
                
                totalCost = c+costToNode
                if totalCost < costs[dest] and ksofar <= k:
                    # print("dest ", dest)
                    # print("cost ", costToNode)
                    costs[dest] = totalCost
                    heap.append((totalCost, dest, ksofar+1))
        
        # print(costs)
        
        if costs[dst] == math.inf:
            return -1
        return costs[dst]
