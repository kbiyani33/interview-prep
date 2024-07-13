from typing import List
class Solution:
    def count(self, nums: List[int], n:int, target: int) -> List[int]:
        def firstOccurence(nums, target):
            res = -1
            start, end = 0, n-1
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
            start, end = 0, n-1
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
        if first==-1 or last==-1:
            return 0
        return last-first+1