from typing import List
from sys import *
from collections import *
from math import *


def brute_force(nums: List[int], k: int) -> int:
    # Write your code here
    maxLen = 0
    n = len(nums)

    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            if curSum == k:
                maxLen = max(maxLen, j - i + 1)
    return maxLen


def prefixSumSolution(nums: List[int], k: int) -> int:
    # Write your code here
    prefixSumMap = {}
    prefSum = 0
    maxLen = 0

    for i in range(len(nums)):
        prefSum += nums[i]
        if prefSum == k:
            maxLen = max(
                maxLen, i + 1
            )  # basically all +,- operations has given us the sum as k till now. So maxLen will be the whole array so far.
        elif prefSum - k in prefixSumMap:
            maxLen = max(maxLen, i - (prefixSumMap[prefSum - k]))
        if prefSum not in prefixSumMap:
            prefixSumMap[prefSum] = i
    # print(prefixSumMap)
    return maxLen


def OptimalSolutionWithOnlyWholeNumbers(a: List[int], k: int) -> int:
    # Write your code here
    curSum, left, right = 0, 0, 0
    n = len(a)
    ans = 0

    while right < n:
        curSum += a[right]
        while curSum > k and left <= right:
            curSum -= a[left]
            left += 1

        if curSum == k:
            ans = max(ans, right - left + 1)
        right += 1

    return ans


class Solution:
    def lenOfLongSubarr(self, arr: List[int], n: int, k: int):
        # Complete the function
        maxLen = 0
        prefixSum, prefixSumMap = 0, {}

        for i in range(n):
            prefixSum += arr[i]
            # Case 1, the prefixSum = k that means that entire array so far is the subarray giving the sum k
            if prefixSum == k:
                maxLen = max(maxLen, i + 1)
            else:
                remaining = prefixSum - k
                # Now find if there is en entry containing remaining sum, if yes, that means it makes this a valid subarray from that index to current index
                if remaining in prefixSumMap:
                    maxLen = max(maxLen, i - prefixSumMap[remaining])
            if (
                prefixSum not in prefixSumMap
            ):  # we want the left most since we want the longest subarray.
                prefixSumMap[prefixSum] = i

        return maxLen
