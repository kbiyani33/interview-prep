"""
Very similar to search in rotated sorted array
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # base case if n==1
        if n==1:
            return nums[0]
        ans = float("inf")
        start, end = 0, n-1
        while start<=end:
            mid = start + (end-start)//2
            # Find which portion is sorted
            if nums[mid] < nums[end]:
                ans = min(ans, nums[mid]) # Since right is sorted, mid will be the minima
                end = mid-1 # move left
            else:# nums[mid] > nums[start]
                ans = min(ans, nums[start]) # Since left is sorted, start will be the minima
                start = mid+1 # move right
        return ans