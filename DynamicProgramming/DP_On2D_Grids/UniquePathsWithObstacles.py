from typing import List
class Solution:
    def recursiveSolution(self, obstacleGrid: List[List[int]], row:int, col:int, dp:List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Now 3 cases. 
        # If theres an obstacle at current index, return 0
        # If theres an obstacle at the m-1, n-1 then also 0
        # If the current index is equal to m-1 and n-1 and it's not an obstacle then return 1
        
        if (obstacleGrid[m-1][n-1]) == 1 or (row>=m or col>=n) or (obstacleGrid[row][col] == 1):
            return 0
        if row==m-1 and col==n-1:
            return 1
        
        if dp[row][col] != -1:
            return dp[row][col]
        
        ans = 0
        ans += self.recursiveSolution(obstacleGrid, row+1, col, dp)
        ans += self.recursiveSolution(obstacleGrid, row, col+1, dp)
        dp[row][col] = ans
        return ans


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*n for i in range(m)]
        return self.recursiveSolution(obstacleGrid, 0, 0, dp)
    
    def tabulationBottomUpDP(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        # Step1 is to copy the base cases as it is
        if (m==0 and n==0) or obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j+1]+dp[i+1][j]
        return dp[0][0]
                
        