# MEMIOZATION
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lis_recursive(arr, n, index, prev, dp):
            if index == n:
                return 0
            if dp[index][prev] != -1:
                return dp[index][prev]
            notTake = lis_recursive(
                arr, n, index + 1, prev, dp
            )  # This means that the current index is not being taken in the LIS
            if prev == n or arr[index] > arr[prev]:
                take = 1 + lis_recursive(arr, n, index + 1, index, dp)
                ans = max(take, notTake)
            else:
                ans = notTake
            dp[index][prev] = ans
            return ans


        def longestIncreasingSubsequence(arr, n):
            dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
            return lis_recursive(arr, n, 0, n, dp)
        
        return longestIncreasingSubsequence(nums, len(nums))
    
# TABULATION
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def BottomUpTabulation(arr, n):
            dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
            for i in range(n, -1, -1):
                for j in range(n, -1, -1):
                    if i == n:
                        dp[i][j] = 0
                        continue
                    notTake = dp[i + 1][j]
                    if j == n or arr[i] > arr[j]:
                        take = 1 + dp[i + 1][i]
                        ans = max(take, notTake)
                    else:
                        ans = notTake
                    dp[i][j] = ans
            return dp[0][n]
        return BottomUpTabulation(nums, len(nums))
        
# TABLE METHOD OF 1D-DP(VERY FAMOUS)
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)