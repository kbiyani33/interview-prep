from typing import List
from math import inf
class Solution:
    def recursive(self, matrix:List[List[int]], row:int, col:int, dp) -> int:
        if len(matrix)==0:
            return 0
        if row>=len(matrix) or col<0 or col>=len(matrix[0]):
            return inf
        
        if row==len(matrix)-1:
            dp[row][col] = matrix[row][col]
            return dp[row][col]

        if dp[row][col] != -inf:
            return dp[row][col]
        
        currentAns = matrix[row][col]
        ans1 = currentAns+self.recursive(matrix, row+1, col, dp)
        ans2 = currentAns+self.recursive(matrix, row+1, col+1, dp)
        ans3 = currentAns+self.recursive(matrix, row+1, col-1, dp)
        dp[row][col] = min(ans1, ans2, ans3)
        return dp[row][col]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = inf
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-inf]*(cols+1) for i in range(rows+1)]
        for i in range(cols):
            ans = min(ans, self.recursive(matrix, 0, i, dp))
        return ans
    
    def tabulationBottomUp(self, matrix:List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[inf]*(n+1) for i in range(m+1)]

        """
        We want to return the minimum at 0th row, so we start row from last to top and col can be in any direction
        """
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1: # last row
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j+1], dp[i+1][j-1])
        ans = inf
        for j in range(n):
            ans = min(ans, dp[0][j])
        return ans
        