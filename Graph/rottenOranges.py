from typing import List
from collections import deque
class Solution:
    
    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid:List[List[int]]):
		m, n = len(grid), len(grid[0])
		visited = [[False]*n for i in range(m)]
		rottenQ = deque()
		freshCounter = 0
		timeTaken = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 2: # rotten oranges
					rottenQ.append((i, j, 0))
					visited[i][j] = True
				elif grid[i][j] == 1:
					freshCounter += 1
		if freshCounter == 0: # if we don't have any fresh, then time taken is 0
			return 0
		while(len(rottenQ) > 0):
			row, col, t = rottenQ.popleft()
			timeTaken = max(timeTaken, t)
			neighbors = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
			for i in neighbors:
				nr, nc = i[0], i[1]
				if nr >=0 and nr < m and nc>=0 and nc<n and grid[nr][nc]==1 and not visited[nr][nc]:
					grid[nr][nc] = 2
					visited[nr][nc] = True
					rottenQ.append((nr, nc, t+1))
		for i in range(m):
			for j in range(n):
				if grid[i][j]==1:
					return -1

		return timeTaken
			