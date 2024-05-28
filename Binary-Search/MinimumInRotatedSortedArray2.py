from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        start, end = 0, n-1
        ans = float("inf")
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==nums[start] and nums[mid]==nums[end]:
                ans = min(ans, nums[mid])
                start+=1
                end-=1
                continue
            if nums[start] <= nums[mid]: # left portion is sorted
                ans = min(ans, nums[start])
                start = mid+1
            else:
                ans = min(ans, nums[mid])
                end = mid-1

        return ans