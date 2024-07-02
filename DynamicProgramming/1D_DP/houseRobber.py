from typing import List
class Solution:
    def recursive(self, nums:List[int], index:int, dp:List[int]) -> int:
        if index>=len(nums):
            return 0
        if dp[index] != -1:
            return dp[index]
        pick, notPick = nums[index]+self.recursive(nums, index+2, dp), self.recursive(nums, index+1,dp)
        dp[index] = max(pick, notPick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        return self.recursive(nums, 0, dp)
    
    def tabulationDPBottomUP(self, nums:List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        return dp[0]
        