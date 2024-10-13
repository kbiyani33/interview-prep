from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps, left, right = 0, 0, 0
        n = len(nums)

        while right < n-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i + nums[i])
            jumps += 1
            left, right = right+1, farthest
        return jumps