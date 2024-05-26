from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nextPosPosition = 0
        nextNegPosition = 1
        arr = [None] * len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                arr[nextPosPosition] = nums[i]
                nextPosPosition += 2
            else:
                arr[nextNegPosition] = nums[i]
                nextNegPosition += 2

        return arr
