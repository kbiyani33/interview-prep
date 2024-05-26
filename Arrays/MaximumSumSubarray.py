from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = -math.inf, 0
        start, end = -1, -1
        for i in range(len(nums)):
            if curSum == 0:
                start = i
            curSum += nums[i]
            if curSum > maxSum:
                end = i
                maxSum = curSum
            maxSum = max(maxSum, curSum)
            curSum = 0 if curSum < 0 else curSum
        print(nums[start : end + 1])
        return maxSum
