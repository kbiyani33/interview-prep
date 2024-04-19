import sys
from typing import List
from collections import deque

sys.setrecursionlimit(10**8)
class Solution:
    def dfs_traversal(self, u:int, v:int, visited:List[List[bool]], grid:List[List[int]]):
        if visited[u][v]:
            return
        m, n = len(grid), len(grid[0])
        visited[u][v] = True
        for diffRow in range(-1, 2):
            for diffCol in range(-1, 2):
                nRow, nCol = u+diffRow, v+diffCol
                if nRow >= 0 and nRow < m and nCol >= 0 and nCol < n and not visited[nRow][nCol] and grid[nRow][nCol]==1:
                    self.dfs_traversal(u=nRow, v=nCol, visited=visited, grid=grid)
        
    def bfs_traversal(self, u:int, v:int, visited:List[List[bool]], grid:List[List[int]]):
        m, n = len(grid), len(grid[0])
        q = deque()
        q.append((u, v))
        while(len(q) > 0):
            row, col = q.popleft()
            for diffRow in range(-1, 2):
                for diffCol in range(-1, 2):
                    nRow = row + diffRow
                    nCol = col + diffCol
                    
                    if nRow >= 0 and nCol >= 0 and nRow < m and nCol < n and grid[nRow][nCol]==1 and not visited[nRow][nCol]:
                        visited[nRow][nCol] = True
                        q.append((nRow, nCol))
            
    def numIslands(self,grid:List[List[int]]):
        #code here
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*(n) for i in range(m)]
        counter = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    counter += 1
                    self.dfs_traversal(u=i, v=j, visited=visited, grid=grid)
        return counter