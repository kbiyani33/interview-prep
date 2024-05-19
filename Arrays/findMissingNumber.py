"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

from typing import List


class Solution:
    def brute(self, nums: List[int]) -> int:
        # Quadratic time
        n = len(nums)
        # n becomes the maximum value from 0 t0 n included
        for i in range(n):
            if i not in nums:
                return i
        return len(nums)  # needed in case we don't have the last value itself

    def better(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for i in range(
            len(nums)
        ):  # in in list is linear, in set is constant thus works
            if i not in numsSet:
                return i
        return len(nums)  # needed in case we don't have the last value itself

    def optimal1(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n * (n + 1) / 2) - sum(nums))

    def missingNumber(self, nums: List[int]) -> int:
        xor1, xor2 = 0, 0
        n = len(nums)
        for i in range(n):
            xor1 ^= i
            xor2 ^= nums[i]
        xor1 ^= n
        return xor1 ^ xor2
