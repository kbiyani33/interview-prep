from typing import List
import math, heapq


class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        # code here
        efforts = [[math.inf] * columns for i in range(rows)]
        efforts[0][0] = 0
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        while len(heap) > 0:
            effort, r, c = heapq.heappop(heap)
            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for near in neighbors:
                nr, nc = near[0], near[1]
                if nr >= 0 and nr < rows and nc >= 0 and nc < columns:
                    totalEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if totalEffort < efforts[nr][nc]:
                        efforts[nr][nc] = totalEffort
                        heapq.heappush(heap, (totalEffort, nr, nc))

        return efforts[-1][-1]
