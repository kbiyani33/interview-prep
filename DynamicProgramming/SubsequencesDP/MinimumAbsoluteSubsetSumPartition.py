from typing import List
from math import inf
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n, totalSum = sum(nums), len(nums)

        dp = [[False for j in range(totalSum+1)] for i in range(n+1)]

        # Base case 1 -> I am looking for sum to be 0. Which is always true :)
        for i in range(n+1):
            dp[i][0] = True
        
        # Base case 2 -> I am looking for non 0 sum with 0 elements in the array. Which is always False :)
        for j in range(1, totalSum+1):
            dp[0][j] = False

        for i in range(n-1, -1, -1):
            for j in range(1, totalSum+1):
                if nums[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j-nums[i]]
        
        minDiff = inf
        for j in range(0, totalSum+1):
            s1, s2 = j, totalSum-j
            if dp[0][s1]:
                minDiff = min(minDiff, abs(s1-s2))
        return minDiff