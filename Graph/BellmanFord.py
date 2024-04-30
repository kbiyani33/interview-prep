"""
Given a weighted and directed graph of V vertices and E edges.
Find the shortest distance of all the vertex's from the source vertex S. 
If a vertices can't be reach from the S then mark the distance as 10^8. 

Note: If the Graph contains a negative cycle then return an array consisting of only -1.
"""

from typing import List
import math

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V:int, edges:List[List[int]], S:int):
        #code here
        distances = [100000000]*V # can be math.inf also. According to the question this is fine.
        parents = [-1]*V
        
        distances[S] = 0
        
        for i in range(V-1):
            for edge in edges:
                src, dest, wt = edge[0], edge[1], edge[2]
                if distances[src] == 100000000:
                    continue
                if distances[src]+wt < distances[dest]:
                    distances[dest] = distances[src]+wt
                    parents[dest] = src
        
        # check for negative cycle
        distance_updated = distances.copy()
        for edge in edges:
            src, dest, wt = edge[0], edge[1], edge[2]
            if distance_updated[src] == 100000000:
                continue
            if distance_updated[src]+wt < distance_updated[dest]:
                return [-1]
        
        # print(parents)
        return distances