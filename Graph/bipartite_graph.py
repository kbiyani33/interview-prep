from collections import deque
from typing import List

class Solution:
	def dfs_solution(self, V:int, adj:List[List[int]], color:List[int], starting:int, colorForStarting:int) -> bool :
		color[starting] = colorForStarting
		nextColor = 0 if colorForStarting==1 else 1
		for near in adj[starting]:
			if color[near] == -1:
				if not self.dfs_solution(V, adj, color, near, nextColor):
					return False
			elif color[near] == color[starting]:
				return False
		return True
	def bfs_bipartite(self, V:int, adj:List[List[int]], color:List[int], starting:int) -> bool:
		q = deque()
		q.append(starting) # append starting to the q and make it's color as True for now
		color[starting] = 0
		
        # now traverse through the neighbors of starting and color them
		while len(q) > 0:
			current = q.popleft()
			for near in adj[current]: # traverse through the neighbors of current
				if color[near] == -1:
					q.append(near)
					color[near] = 1 if color[current] == 0 else 0
				elif color[near]==color[current]:
					return False
		return True
		
	def isBipartite(self, V:int, adj:List[List[int]]) -> bool:
		color = [-1]*V
		for i in range(V):
			if color[i] == -1 : # i.e. its not yet been colored
				ans = self.dfs_solution(V, adj, color, i, 0)
				if not ans:
					return False
		return True
		
