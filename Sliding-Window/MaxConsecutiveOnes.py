from collections import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n, left, right = len(nums), 0, 0
        maxVal = 0
        while right < n:
            if nums[right] == 0:
                left = right+1
            else:
                size = right-left+1
                maxVal = max(maxVal, size)
            right += 1
        return maxVal