class DisjointSet:

    def __init__(self, N:int) -> None:
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1]*(N+1)

    def findParent(self, node:int) -> int:
        parent = self.parent
        if node==parent[node]:
            return node
        parent[node] = self.findParent(parent[node])
        return parent[node]
    
    def unionBySize(self, u:int, v:int):
        parent,size = self.parent, self.size
        parU = self.findParent(u)
        parV = self.findParent(v)

        if parU==parV:
            return
        
        if parU<parV:
            parent[parU]=parV
            size[parV] += size[parU]
        else:
            parent[parV] = parU
            size[parU] += size[parV]

from typing import List
class Solution:
    def Solve(self, n:int, adj:List[List[int]]) -> int:
        ds = DisjointSet(n)
        extraEdges = 0
        for edge in adj:
            u,v = edge[0],edge[1]
            if ds.findParent(u)==ds.findParent(v):
                extraEdges+=1
            ds.unionBySize(u,v)
        nC = 0
        for i in range(n):
            if ds.findParent(i)==i:
                nC+=1
        # print(extraEdges)
        # print(nC)
        if extraEdges >= nC-1:
            return nC-1
        return -1