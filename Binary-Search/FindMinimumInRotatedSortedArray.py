"""
Very similar to search in rotated sorted array
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while(start < end):
            middle = start + (end-start)//2
            if nums[middle] <= nums[end]:
                end = middle
            elif nums[middle] > nums[end]:
                start = middle + 1
        return nums[start]