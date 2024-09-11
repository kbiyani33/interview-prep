import math
class Solution:
    def recursive(self, height, n, k, index, dp):
        if index == n-1 :
            return 0
        if dp[index] != -1:
            return dp[index]
        minI = math.inf
        for j in range(1, k+1):
            newPos = index + j
            if newPos <= n-1:
                ans = abs(height[newPos]-height[index]) + self.recursive(height, n, k, newPos, dp)
                minI = min(minI, ans)
        dp[index] = minI
        return minI
    def minimizeCost(self, height, n, k):
        # code here
        dp = [-1]*n
        return self.recursive(height, n, k, 0, dp)