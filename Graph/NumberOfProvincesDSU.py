"""
Given an undirected graph with V vertices. 
We say two vertices u and v belong to a single province if there is a path from u to v or v to u. 
Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.
"""
class DisjointSet:

    def __init__(self, N:int):
        self.N = N
        self.parent = [i for i in range(N+1)]
        self.size = [1] * (N+1)
    
    def findParent(self, u:int) -> int:
        parent = self.parent
        if parent[u] == u:
            return u
        parent[u] = self.findParent(parent[u])
        return parent[u]
    
    def unionBySize(self, u:int, v:int):
        parent, size = self.parent, self.size

        parentU = self.findParent(u)
        parentV = self.findParent(v)

        if parentU==parentV:
            return
        
        if size[parentU] < size[parentV]:
            parent[parentU] = parentV
            size[parentV] += size[parentU]
        else:
            parent[parentV] = parentU
            size[parentU] += size[parentV]

class Solution:
    def numProvinces(self, adj, V):
        ds = DisjointSet(V)
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    ds.unionBySize(i,j)
        counter = 0 
        for i in range(V):
            if ds.findParent(i) == i:
                counter += 1
        return counter



