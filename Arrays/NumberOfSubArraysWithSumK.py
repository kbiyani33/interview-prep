from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixSumMap = {}
        prefixSumSoFar = 0
        n = len(nums)

        for i in range(n):
            prefixSumSoFar += nums[i]
            # case 1 -> prefixSumSoFar is equal to k
            if prefixSumSoFar == k:
                ans += 1
            remaining = prefixSumSoFar - k
            for j in range(i):
                if prefixSumMap[j] == remaining:
                    ans += 1
            prefixSumMap[i] = prefixSumSoFar

        return ans
