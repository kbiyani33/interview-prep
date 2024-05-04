import math

class DisjointSet:
    def __init__(self, N:int):
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1] * (N+1)
    
    def findParent(self, node:int) -> int:
        parent = self.parent
        if parent[node]==node:
            return node
        parent[node] = self.findParent(parent[node])
        return parent[node]
        
    def unionBySize(self, u:int, v:int):
        parent, size = self.parent, self.size
        parU = self.findParent(u)
        parV = self.findParent(v)
        
        if parU==parV:
            return
        
        if size[parU]<size[parV]:
            parent[parU] = parV
            size[parV] += size[parU]
        else:
            parent[parV] = parU
            size[parU] += size[parV]


class Solution:
    def maxRemove(self, adj, n):
        # Code here
        maxR, maxC = -math.inf, -math.inf
        for pos in adj:
            r,c = pos[0], pos[1]
            maxR = max(maxR, r)
            maxC = max(maxC, c)

        totalNodes = maxR + maxC + 2
        rows = [i for i in range(maxR+1)]
        cols = [i+maxR+1 for i in range(maxC)]
        
        ds = DisjointSet(totalNodes)
        stoneRowCols = {}
        for pos in adj:
            r,c = pos[0], pos[1]
            ds.unionBySize(r, c+maxR+1)
            stoneRowCols[r] = 1
            stoneRowCols[c+maxR+1] = 1
        
        components = 0
        # m = 0
        for i in stoneRowCols:
            if ds.findParent(i)==i:
                components += 1
        return n-components