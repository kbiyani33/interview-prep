from os import *
from sys import *
from collections import *
from math import *

from typing import List

class Solution:
    def perfectSum(self, arr, n, target):
        # code here
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(n-1, -1, -1):
            for j in range(target+1):
                if arr[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = (dp[i+1][j] +dp[i+1][j-arr[i]])
        return dp[0][target]

    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        # write your code here
        totalSum = sum(arr)
        if (totalSum+d)%2==1 or totalSum+d < 0:
            return 0
        modifiedTarget = (totalSum+d)//2
        return self.perfectSum(arr, len(arr), modifiedTarget)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.countPartitions(len(nums), target, nums)