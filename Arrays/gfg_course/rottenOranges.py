from typing import List
from collections import deque
import math, heapq


class Solution:

    # Function to find minimum time required to rot all oranges.
    def orangesRotting(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        # find a rotten orange
        q = deque()
        freshCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # since this guy is already rotten
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    freshCount += 1

        if not q and freshCount == 0:
            return 0
        timeTaken = 0
        while q:
            r, c, t = q.popleft()
            timeTaken = max(timeTaken, t)
            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for adj in neighbors:
                nr, nc = adj[0], adj[1]
                if (
                    nr >= 0
                    and nr < m
                    and nc >= 0
                    and nc < n
                    and not visited[nr][nc]
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    visited[nr][nc] = True
                    q.append((nr, nc, t + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return timeTaken
