from typing import List
from collections import Counter


class Solution:
    def brute(self, nums: List[int]) -> int:
        n = len(nums)
        target = n // 2 + 1
        for i in range(n):
            count, elem = 0, nums[i]
            for j in range(n):
                if nums[j] == elem:
                    count += 1
            if count >= target:
                return elem

    def better(self, nums: List[int]) -> int:
        freq = Counter(nums)
        target = len(nums) // 2 + 1
        for k in freq:
            if freq[k] >= target:
                return k
        return -1

    def majorityElement(self, nums: List[int]) -> int:
        # Moore's voting algorithm
        element, count = -1, 0
        for i in range(len(nums)):
            if count == 0:
                element = nums[i]
                count = 1
            elif nums[i] == element:
                count += 1
            else:
                count -= 1

        return element
