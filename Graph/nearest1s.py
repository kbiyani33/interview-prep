from collections import deque
from typing import List

class Solution:
    def nearest_using_bfs(self, grid:List[List[int]], visited:List[List[bool]], result:List[List[int]]):
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # first make result for this to be 0
                    result[i][j] = 0 # since closest 1 to any 1 in the input matrix is itself
                    # append the i, j with the distance to get to this
                    q.append((i, j, 0))
                    # make it as visited
                    visited[i][j] = True
        
        while(len(q) > 0):
            r, c, d = q.popleft()
            neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
            for neighbor in neighbors:
                nr, nc = neighbor[0], neighbor[1]
                if nr >=0 and nr < m and nc >= 0 and nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    # first make it visited
                    visited[nr][nc] = True
                    # update the grid cell to become 1
                    grid[nr][nc] = 1
                    # make it's result to be d+1
                    result[nr][nc] = d+1
                    # append it to the queue with it's distance as d+1
                    q.append((nr, nc, d+1))

    #Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid:List[List[int]]):
        #Code here
        m, n = len(grid), len(grid[0])
        grid_copy = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid_copy[i][j] = grid[i][j]
        result = [[-1]*n for i in range(m)]
        visited = [[False]*n for i in range(m)]
        self.nearest_using_bfs(grid=grid_copy, visited=visited, result=result)
        return result
    
class SolutionLC:
    def nearest_using_bfs(self, grid:List[List[int]], visited:List[List[bool]], result:List[List[int]]):
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # first make result for this to be 0
                    result[i][j] = 0 # since closest 1 to any 1 in the input matrix is itself
                    # append the i, j with the distance to get to this
                    q.append((i, j, 0))
                    # make it as visited
                    visited[i][j] = True
        
        while(len(q) > 0):
            r, c, d = q.popleft()
            neighbors = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
            for neighbor in neighbors:
                nr, nc = neighbor[0], neighbor[1]
                if nr >=0 and nr < m and nc >= 0 and nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                    # first make it visited
                    visited[nr][nc] = True
                    # update the grid cell to become 1
                    grid[nr][nc] = 0
                    # make it's result to be d+1
                    result[nr][nc] = d+1
                    # append it to the queue with it's distance as d+1
                    q.append((nr, nc, d+1))
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        grid_copy = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                grid_copy[i][j] = mat[i][j]
        result = [[-1]*n for i in range(m)]
        visited = [[False]*n for i in range(m)]
        self.nearest_using_bfs(grid=grid_copy, visited=visited, result=result)
        return result