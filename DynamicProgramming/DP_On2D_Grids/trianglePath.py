from typing import List
from math import inf
class Solution:
    def recursiveSolution(self, triangle: List[List[int]], row:int, col:int, dp:List[List[int]]) -> int:
        if len(triangle)==0 or row>=len(triangle) or col>=len(triangle[row]):
            return 0
        if dp[row][col] != -inf:
            return dp[row][col]
        # Now there are 2 possibilities. 
        # Either go down straight(row+1, col)
        # Or go down right(row+1, col+1). And get the minimum value
        currentAns = triangle[row][col]
        ans1 = currentAns + self.recursiveSolution(triangle, row+1, col, dp)
        ans2 = currentAns + self.recursiveSolution(triangle, row+1, col+1, dp)
        dp[row][col] = min(ans1, ans2)
        return dp[row][col]

        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])
        dp = [[-inf]*(n+1) for i in range(m+1)]
        return self.recursiveSolution(triangle, row=0, col=0, dp=dp) # since I am always starting at the 0th row and 0th column
    
    def tabulationDp(self, triangle:List[List[int]]) -> int:
        m, n = len(triangle), len(triangle[-1])
        dp = [[inf]*(n+1) for i in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
        