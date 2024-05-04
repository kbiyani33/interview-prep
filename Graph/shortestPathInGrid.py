# User function Template for python3

from typing import List
from collections import deque
import math

"""
Why q and not priority q ?
Because, in this question, we are having no weight matrix. Every weight is actually equal.
So, no point of adding the O(logN) setup of removing the minimum element. Since there will be no minimum distance element.
So simple queue works better in fact because of O(1) removal where all weights are equal.
"""


class Solution:
    def djikstra_traversal(
        self, grid: List[List[int]], source: List[int], destination: List[int]
    ) -> int:
        m, n = len(grid), len(grid[0])
        distances = [[math.inf] * n for i in range(m)]
        distances[source[0]][source[1]] = 0
        q = deque()
        q.append((0, source[0], source[1]))

        while len(q) > 0:
            distance, r, c = q.popleft()
            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for near in neighbors:
                nr, nc = near[0], near[1]
                distanceTotal = 1 + distance  # from previous to this
                if (
                    nr >= 0
                    and nr < m
                    and nc >= 0
                    and nc < n
                    and grid[nr][nc] == 1
                    and distanceTotal < distances[nr][nc]
                ):
                    distances[nr][nc] = distanceTotal
                    q.append((distanceTotal, nr, nc))

        if distances[destination[0]][destination[1]] == math.inf:
            return -1
        return distances[destination[0]][destination[1]]

    def shortestPath(
        self, grid: List[List[int]], source: List[int], destination: List[int]
    ) -> int:
        # code here
        return self.djikstra_traversal(grid, source, destination)
