from math import inf
from typing import List
class Solution:
    def tabulationBottomUpDP(self, arr:List[int], k:int):
        # Step 1 is copy the base case as it it
        n = len(arr)
        if n==0:
            return 0
        if k==n:
            return max(arr)*n
        if k==1:
            return sum(arr)
        
        # I want to return dp[0] which means i want to go from n-1 to 0
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            kmax, maxI = -inf, -inf
            for j in range(i, min(n, i+k)):
                kmax = max(kmax, arr[j])
                partitionElementCount = j-i+1
                ans = partitionElementCount*kmax + dp[j+1]
                maxI = max(maxI, ans)
            dp[i] = maxI
        return dp[0]


    def recursiveSolution(self, arr:List[int], k:int, index:int, dp:List[int]) -> int:
        n = len(arr)
        if index >= n:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        # remaining = n-index
        # if remaining <= k:
        #     kmax = -inf
        #     for j in range(index, n):
        #         kmax = max(kmax, arr[j])
        #     dp[index] = remaining*kmax
        #     return dp[index]
        # The upper block is actually elegently fixed by the min used in the range given below
        # Now i can either partition at index, or at index+1 and so on till index+k, not till the end of the array
        maxI = -inf
        kmax = -inf
        for j in range(index, min(index+k, n)):
            kmax = max(kmax, arr[j])
            elementsGroupedInCurrentPartition  = j-index+1
            ans = elementsGroupedInCurrentPartition*kmax + self.recursiveSolution(arr, k, j+1, dp)
            maxI = max(maxI, ans)
        dp[index] = maxI
        return maxI


    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == 1: 
            return sum(arr)
        if k==n:
            return n*max(arr)
        dp = [-1]*(n+1)
        return self.recursiveSolution(arr, k, 0, dp)