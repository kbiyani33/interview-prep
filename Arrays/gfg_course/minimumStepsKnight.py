from typing import List
from collections import deque
import math, heapq


class Solution:

    def validateRowCol(self, row: int, col: int, N: int) -> bool:
        return row >= 0 and row < N and col >= 0 and col < N

    def minStepToReachTarget(self, KnightPos: List[int], TargetPos: int, N: int):
        KnightPos = [i - 1 for i in KnightPos]
        TargetPos = [i - 1 for i in TargetPos]
        if not self.validateRowCol(
            row=KnightPos[0], col=KnightPos[1], N=N
        ) or not self.validateRowCol(row=TargetPos[0], col=TargetPos[1], N=N):
            return -1
        if TargetPos == KnightPos:
            return 0

        minJumps = math.inf
        visited = [[False] * N for i in range(N)]
        heap = []
        heapq.heappush(heap, (0, KnightPos[0], KnightPos[1]))
        visited[KnightPos[0]][KnightPos[1]] = True
        while heap:
            jumps, row, col = heapq.heappop(heap)
            if [row, col] == TargetPos:
                return jumps
            # now getting the next possible positions for knight
            knightJumps = [
                [1, 2],
                [1, -2],
                [-1, 2],
                [-1, -2],
                [2, 1],
                [2, -1],
                [-2, 1],
                [-2, -1],
            ]
            for adj in knightJumps:
                nr, nc = row + adj[0], col + adj[1]
                if self.validateRowCol(nr, nc, N) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (jumps + 1, nr, nc))

        return minJumps
