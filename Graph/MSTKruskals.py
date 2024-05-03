"""
Given a weighted, undirected and connected graph of V vertices and E edges. 
The task is to find the sum of weights of the edges of the Minimum Spanning Tree. 
Given adjacency list adj as input parameters . 
Here adj[i] contains vectors of size 2, where the first integer in that vector denotes the end of the edge and the second integer denotes the edge weight.
"""
from typing import List, Tuple
from operator import itemgetter

class DisjointSet:

    def __init__(self, N:int):
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1]*(N+1)
    
    def findParent(self, node:int) -> int:
        parent = self.parent
        if parent[node]==node:
            return node
        parent[node] = self.findParent(parent[node])
        return parent[node]
    
    def unionBySize(self, u:int, v:int):
        parent, size = self.parent, self.size
        parentU = self.findParent(u)
        parentV = self.findParent(v)

        if parentU == parentV:
            return
        
        if size[parentU] < size[parentV]:
            parent[parentU] = parentV
            size[v] += size[u]
        else:
            parent[parentV] = parentU
            size[u] += size[v]


class Solution:
    
    def convertAdjListToListOfEdgesSortedByWeights(self, V:int, adj:List[List[int]]) -> List[Tuple[int]]:
        # print(adj)
        edges = []
        for i in range(V):
            for j in adj[i]:
                src, dest, weight = i, j[0], j[1]
                edges.append((weight, src, dest))
        edges.sort(key=itemgetter(0))
        return edges
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V:int, adj:List[List[List[int]]]):
        sorted_edges = self.convertAdjListToListOfEdgesSortedByWeights(V=V, adj=adj)
        # print(sorted_edges)
        ds = DisjointSet(N=V)
        mstWeight = 0
        for edge in sorted_edges:
            wt,u,v=edge[0], edge[1], edge[2]

            if ds.findParent(u) != ds.findParent(v):
                mstWeight += wt
                ds.unionBySize(u,v)
        # print(ds.parent)
        return mstWeight

