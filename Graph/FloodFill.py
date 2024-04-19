from typing import List
from collections import deque
class Solution:
    def dfs_traversal(self, image:List[List[int]], sr:int, sc:int, newColor:int, visited:List[List[bool]], initial:int):
        if visited[sr][sc]:
            return
        m, n = len(image), len(image[0])
        visited[sr][sc] = True
        image[sr][sc] = newColor
        movements = [[sr-1, sc], [sr, sc], [sr+1, sc], [sr, sc-1], [sr, sc+1]]
        for i in movements:
            row, col = i[0], i[1]
            if row >= 0 and row < m and col >= 0 and col < n and image[row][col]==initial:
                self.dfs_traversal(image, row, col, newColor, visited, initial)
                
    def bfs_traversal(self, image:List[List[int]], sr:int, sc:int, newColor:int, visited:List[List[bool]]):
        m, n = len(image), len(image[0])
        q = deque()
        q.append((sr, sc))
        initialColor = image[sr][sc]
        while(len(q) != 0):
            row, col = q.popleft()
            visited[row][col] = True
            image[row][col] = newColor
            movements = [[row-1, col], [row, col], [row+1, col], [row, col-1], [row, col+1]]
            
            for i in movements:
                nr, nc = i[0], i[1]
                if nr>=0 and nr<m and nc>=0 and nc<n and image[nr][nc]==initialColor and not visited[nr][nc]:
                    q.append((nr, nc))
            
            
    def floodFill(self, image:List[List[int]], sr:int, sc:int, newColor:int):
        m, n = len(image), len(image[0])
        visited = [[False]*n for i in range(m)]
        self.dfs_traversal(image, sr, sc, newColor, visited, image[sr][sc])
        return image