from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target or nums[start]==target or nums[end]==target:
                return True
            
            # increment and decrement start and end until the 3 values are equal
            if nums[mid]==nums[start] and nums[mid]==nums[end]:
                start+=1
                end-=1
                continue
            
            # Find the sorted part
            if nums[mid] <= nums[end]: # right half is sorted
                if nums[mid] < target < nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            elif nums[mid] >= nums[start] : # left half is sorted
                if nums[start] < target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return False

            
