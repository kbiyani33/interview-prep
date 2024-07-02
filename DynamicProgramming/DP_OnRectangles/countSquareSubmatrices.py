from typing import List

class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]

        total = 0

        for j in range(n):
            dp[0][j] = matrix[0][j]
            total += dp[0][j]
        for i in range(m):
            dp[i][0] = matrix[i][0]
            total += dp[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0 # since there'll never be a sub matrix that's ending at this
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                total += dp[i][j]
        return total