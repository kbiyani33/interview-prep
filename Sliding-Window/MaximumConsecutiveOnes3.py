from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, zeros = 0, 0, 0
        maxVal = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros+=1
            if zeros > k:
                # move left to 1 above the first index of 0
                if nums[left]==0:
                    zeros-=1
                left += 1
            size = right-left+1
            right += 1
            maxVal = max(maxVal, size)
        return maxVal