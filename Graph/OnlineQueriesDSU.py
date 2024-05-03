"""
You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator(s) and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operation.You need to return an array of size k.
Note : An island means group of 1s such that they share a common side.

 

Example 1:

Input: n = 4
m = 5
k = 4
A = {{1,1},{0,1},{3,3},{3,4}}

Output: 1 1 2 2
Explanation:
0.  00000
    00000
    00000
    00000
1.  00000
    01000
    00000
    00000
2.  01000
    01000
    00000
    00000
3.  01000
    01000
    00000
    00010
4.  01000
    01000
    00000
    00011
"""

from typing import List

#User function Template for python3
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
        
        if size[parU]<size[parV]:
            parent[parU]=parV
            size[parV] += size[parU]
        else:
            parent[parV] = parU
            size[parU] += size[parV]
    

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        ds = DisjointSet(rows*cols)
        visited = [[False]*cols for i in range(rows)]
        islands = 0
        
        queryResults = []
        for query in operators:
            row, col = query[0], query[1]
            node = row*cols + col
            if not visited[row][col]:
                # mark visited and first add 1 to island count
                visited[row][col] = True
                islands += 1
                # Now go up, right, down and left and ensure
                neighbors = [[row-1, col], [row, col+1], [row+1, col], [row, col-1]]
                for near in neighbors:
                    nr, nc = near[0], near[1]
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and visited[nr][nc]:
                        adjNode = nr*cols + nc
                        # confirm if the parent of node and adjacent node is the same
                        if ds.findParent(node) != ds.findParent(adjNode):
                            # print("parents not same so reducing for neighbor")
                            islands -= 1
                            # connect
                            ds.unionBySize(node, adjNode)
            
            queryResults.append(islands)
        return queryResults                
        