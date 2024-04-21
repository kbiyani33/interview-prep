#User function Template for python3
import sys
from typing import List, Tuple
from collections import deque

sys.setrecursionlimit(10**8)
class Solution:
    def bfs_countDistinctIslands(self, grid:List[List[int]], visited:List[List[bool]], baseRow:int, baseCol:int, q:deque) -> Tuple[Tuple[int]]:
        m, n = len(grid), len(grid[0])
        shape = ((0,0),) # from the base
        while(len(q) > 0):
            r,c = q.popleft()
            ngh = [[r, c-1], [r-1, c], [r, c+1], [r+1, c]]
            for i in ngh:
                nr, nc = i[0], i[1]
                if nr >=0 and nr<m and nc>=0 and nc<n and not visited[nr][nc] and grid[nr][nc]==1:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    shape += ((nr-baseRow, nc-baseCol),)
        return shape

    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for i in range(m)]
        q = deque()
        shapeSet = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))
                    shape = self.bfs_countDistinctIslands(grid=grid, visited=visited, baseRow=i, baseCol=j, q=q)
                    # print(shape)
                    shapeSet.add(shape)
        return len(list(shapeSet))
        # return self.countDistinctIslands_dfs(grid)
    
    def dfs_solution(self, grid:List[List[int]], visited: List[List[bool]], baseRow:int, baseCol:int, cr:int, cc:int, shape:List[any]):
        if visited[cr][cc]:
            return
        m, n = len(grid), len(grid[0])
        visited[cr][cc] = True
        shape.append((cr-baseRow, cc-baseCol))
        neighbors = [[cr, cc-1], [cr-1, cc], [cr, cc+1], [cr+1, cc]]
        for i in neighbors:
            nr, nc  =i[0], i[1]
            if nr>=0 and nr<m and nc>=0 and nc<n and not visited[nr][nc] and grid[nr][nc]==1:
                self.dfs_solution(grid=grid, visited=visited, baseRow=baseRow, baseCol=baseCol, cr=nr, cc=nc, shape=shape)
        

    def countDistinctIslands_dfs(self, grid : List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for i in range(m)]
        distinctShapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    self.dfs_solution(grid=grid, visited=visited, baseRow=i, baseCol=j, cr=i, cc=j, shape=shape)
                    # print(shape)
                    distinctShapes.add(tuple(shape)) # we convert to tuple since set needs hashable type which is tuple in python and not list
        return len(distinctShapes)