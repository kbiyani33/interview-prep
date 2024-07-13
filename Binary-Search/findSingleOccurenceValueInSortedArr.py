from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        start, end = 1, n-2
        while start <= end:
            mid = start + (end-start)//2
            # First check if mid is the single element
            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            
            # mid is not single element, so it's repitition exists
            if mid % 2 == 1:
                if nums[mid-1] == nums[mid]: # i.e. even first then odd then the single is on right
                    start = mid+1
                else:
                    end = mid-1
            else:
                if nums[mid+1]==nums[mid]: # i.e. even first then odd then single is on right
                    start = mid+1
                else:
                    end = mid-1
        return -1
        