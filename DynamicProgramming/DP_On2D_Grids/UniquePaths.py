from typing import List
class Solution:
    def recursiveSolution(self, currentRow:int, currentCol:int, m:int, n:int, dp:List[List[int]]) -> int:
        if currentRow>=m or currentCol>=n:
            return 0
        if currentRow==m-1 and currentCol==n-1:
            return 1
        if dp[currentRow][currentCol] != -1:
            return dp[currentRow][currentCol]
        # So now we have a choice. One way is to go right (currentRow, currentCol+1) or down (currentRow+1, currentCol)
        ans = 0
        downRow, downCol = currentRow+1, currentCol
        rightRow, rightCol = currentRow, currentCol+1
        if downRow<m and downCol<n:
            ans += self.recursiveSolution(downRow, downCol, m, n, dp)
        if rightRow<m and rightCol<n:
            ans += self.recursiveSolution(rightRow, rightCol, m, n, dp)
        dp[currentRow][currentCol] = ans
        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]
        return self.recursiveSolution(0, 0, m, n, dp)
    
    def uniquePathsTabulation(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]