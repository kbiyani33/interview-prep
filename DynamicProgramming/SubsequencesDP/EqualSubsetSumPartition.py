from typing import List

class Solution:
    def subSetSum(self, nums:List[int], sumVal:int) -> bool:
        n = len(nums)
        dp = [[False for j in range(sumVal+1)] for i in range(n+1)]
        for i in range(n):
            dp[i][0] = True # Since getting 0 sum is possible
        for j in range(1, sumVal+1):
            dp[0][j] = False
        for i in range(n-1, -1, -1):
            for j in range(1, sumVal+1):
                if nums[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] or dp[i+1][j-nums[i]]
        return dp[0][sumVal]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1:
            return False
        return self.subSetSum(nums, total//2)

        