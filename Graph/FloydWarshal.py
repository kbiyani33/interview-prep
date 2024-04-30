"""
The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. 
The graph is represented as an adjacency matrix of size n*n. 
Matrix[i][j] denotes the weight of the edge from i to j. 
If Matrix[i][j]=-1, it means there is no edge from i to j.
*** Do it in-place. ***
"""


from typing import List
import math
class Solution:
	def shortest_distance(self, matrix:List[List[int]]):
		#Code here
		V = len(matrix)
		# Initialization
		for i in range(V):
			for j in range(V):
				if matrix[i][j] == -1:
					matrix[i][j] = math.inf
				elif i==j:
					matrix[i][j] = 0
		for via in range(V):
			for i in range(V):
				for j in range(V):
					matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])
		for i in range(V):
		    for j in range(V):
		        if matrix[i][j] == math.inf:
		            matrix[i][j] = -1
		      #  if i==j and matrix[i][j] < 0:
		      #      # negative cycle
		      #      return
