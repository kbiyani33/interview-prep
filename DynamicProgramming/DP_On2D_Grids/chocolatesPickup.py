from typing import List
from math import inf
class Solution:
    def recursive(self,grid:List[List[int]], row:int, col1:int, col2:int, dp:List[List[int]]) -> int:
        # First get out of bounds condition.
        if col1<0 or col1>=len(grid[0]) or col2<0 or col2>=len(grid[0]):
            return -inf # I never want to take this path
        if row==len(grid)-1:
            if col1==col2:
                dp[row][col1][col2] = grid[row][col1]
            else:
                dp[row][col1][col2] = grid[row][col1] + grid[row][col2]
            return dp[row][col1][col2]
        
        if dp[row][col1][col2] != -inf:
            return dp[row][col1][col2]
        
        maxAns = -inf
        # Now we go for all possible paths. For each col change for robot1, there are 3 possible changes of col for robot2
        for di in range(-1, 2):
            for dj in range(-1, 2):
                nc1, nc2 = col1+di, col2+dj
                if col1==col2:
                    maxAns = max(maxAns, grid[row][col1]+self.recursive(grid, row+1, nc1, nc2, dp))
                else:
                    maxAns = max(maxAns, grid[row][col1]+grid[row][col2]+self.recursive(grid, row+1, nc1, nc2, dp))
        dp[row][col1][col2] = maxAns
        return dp[row][col1][col2]


    def solve(self, m:int, n:int, grid:List[List[int]]):
        # Code here
        # m rows and n columns
        dp = [[[-inf for _ in range(n+1)] for _ in range(n+1)] for _ in range(m+1)]
        return self.recursive(grid, 0, 0, n-1, dp)
    
    def bottomUpTabulationDP(self, m:int, n:int, grid:List[List[int]]):
        dp = [[[-inf for _ in range(n+1)] for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j1 in range(n-1, -1, -1):
                for j2 in range(n-1, -1, -1):
                    if i==m-1:
                        if j1==j2:
                            dp[i][j1][j2] = grid[i][j1]
                        else:
                            dp[i][j1][j2] = grid[i][j1] + grid[i][j2]
                    else:
                        maxI = -inf
                        for d1 in range(-1, 2):
                            for d2 in range(-1, 2):
                                nc1, nc2 = j1+d1, j2+d2
                                
                                if j1==j2:
                                    val = grid[i][j1] + dp[i+1][nc1][nc2]
                                else:
                                    val = grid[i][j1]+grid[i][j2] + dp[i+1][nc1][nc2]
                                maxI = max(maxI, val)
                        dp[i][j1][j2] = maxI
        return dp[0][0][n-1]