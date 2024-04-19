from collections import deque
from typing import List

class Solution:
    def bfs_number_enclaves(self, grid:List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for i in range(m)]
        q = deque()
        # We only care about 1's on boundary
        for i in range(m):
            if grid[i][0] == 1:
                visited[i][0] = True
                q.append((i, 0))
            if grid[i][n-1] == 1:
                visited[i][n-1] = True
                q.append((i, n-1))

        for j in range(n):
            if grid[0][j] == 1:
                visited[0][j] = True
                q.append((0, j))
            if grid[m-1][j] == 1:
                visited[m-1][j] = True
                q.append((m-1, j))
        
        while(len(q) > 0):
            r,c = q.popleft()
            neighbors = [[r-1,c], [r+1, c], [r, c-1], [r,c+1]]
            for ng in neighbors:
                nr, nc = ng[0], ng[1]
                if nr>=0 and nr<m and nc>=0 and nc<n and grid[nr][nc]==1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        nonVisited = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    nonVisited += 1
        return nonVisited

    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        return self.bfs_number_enclaves(grid)