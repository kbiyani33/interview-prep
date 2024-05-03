"""
You are given an n x n binary grid. A grid is said to be binary if every value in grid is either 1 or 0.

You can change at most one cell in grid from 0 to 1.

You need to find the largest group of connected  1's.

Two cells are said to be connected if both are adjacent to each other and both have same value.

Example 1

Input:
2
1 1
0 1

Output:
4

Explanation:
By changing cell (2,1) ,we can obtain a connected group of 4 1's
1 1
1 1
"""

from typing import List
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
    def MaxConnection(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid) # since it's a N*N square grid, col will be the same
        ds = DisjointSet(n*n)
        
        # first go through the grid and connect all 1's and then get the position of all 0's
        allZeroPositions = []
        grid_copy = grid.copy()
        for i in range(n):
            for j in range(n):
                if grid_copy[i][j] == 1:
                    neighbors = [[i-1,j],[i+1,j], [i,j-1], [i,j+1]]
                    for near in neighbors:
                        nr,nc = near[0], near[1]
                        if nr>=0 and nr<n and nc>=0 and nc<n and grid_copy[nr][nc]==1:
                            node = i*n+j
                            adjNode = nr*n+nc
                            ds.unionBySize(node, adjNode)
                else:
                    allZeroPositions.append([i,j])
        maxSize = -math.inf
        for pos in allZeroPositions:
            parents = set()
            r,c = pos[0], pos[1]
            node = r*n+c
            neighbors = [[r-1,c], [r+1,c], [r, c-1], [r, c+1]]
            for near in neighbors:
                nr,nc = near[0], near[1]
                if nr>=0 and nr<n and nc>=0 and nc<n and grid_copy[nr][nc]==1:
                    adjNode = nr*n+nc
                    parents.add(ds.findParent(adjNode))
            
            # print(parents)
            counter = 0
            for par in parents:
                counter += ds.size[par]
                
            maxSize = max(counter+1, maxSize)
            
        if maxSize==-math.inf:
            return n*n
        return maxSize
        
