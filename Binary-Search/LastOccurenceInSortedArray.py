"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List

def getLastOccurence(nums:List[int], target:int) -> int:
    result = -1
    N = len(nums)
    start, end = 0, N-1
    while(start <= end):
        middle = start + (end-start)//2
        if nums[middle] == target:
            result = middle
            start = middle+1
        elif target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
    return result

if __name__=="__main__":
    arr = [2, 4, 5, 6, 8, 11, 11, 11, 11, 32, 43]
    query = 11
    print(getLastOccurence(arr, query))
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        start, end = 0, N-1
        result = []
        while(start <= end):
            middle = start + (end-start)//2
            if nums[middle] == target:
                # In this case move towards right then move towards left
                
                # moving left
                x = middle
                while(x >= 0  and nums[x] == target):
                    x -= 1
                result.append(x+1)

                # moving right
                x = middle
                while(x < len(nums) and nums[x] == target):
                    x += 1
                result.append(x-1)
                
                return result
            
            if target > nums[middle]:
                start = middle + 1
            else:
                end = middle-1

        return [-1, -1]