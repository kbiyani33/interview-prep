from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = -1
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                found = mid
                break
            if target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        if found==-1:
            return [-1, -1]
        first, last = found, found
        while first>=0 and nums[first]==target:
            first-=1
        while last<len(nums) and nums[last]==target:
            last+=1
        return [first+1, last-1] # +1 and -1 since the condition actually breaks one before and one after in the 2 cases
    
# The above solution is worst case O(N) because it's possible that the array has a majority of target elements and they'll get found quickly. But the while loop is the problem.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurence(nums, target):
            res = -1
            start, end = 0, len(nums)-1
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid]==target:
                    res = mid
                    end = mid-1
                elif target<nums[mid]:
                    end=mid-1
                elif target>nums[mid]:
                    start=mid+1
            return res
        def lastOccurence(nums, target):
            res = -1
            start, end = 0, len(nums)-1
            while start<=end:
                mid = start + (end-start)//2
                if nums[mid]==target:
                    res = mid
                    start = mid+1
                elif target<nums[mid]:
                    end=mid-1
                elif target>nums[mid]:
                    start=mid+1
            return res
        first = firstOccurence(nums, target)
        last = lastOccurence(nums, target)
        return [first, last]
        