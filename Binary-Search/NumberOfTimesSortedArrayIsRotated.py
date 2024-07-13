"""
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

Examples:

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0
"""

# The index of the minimum element is the number of times it had been rotated
from typing import List

class Solution:
    def findKRotation(self,arr:List[int],n:int):
        # code here
        ans, n = -1, len(arr)
        if n <= 1:
            return 0
        
        start, end = 0, n-1
        while start<=end:
            mid = start + (end-start)//2
            # Find the sorted portion
            if arr[mid] < arr[end]: # right half is sorted
                if ans==-1 or (arr[mid] < arr[ans]):
                    ans = mid
                end = mid-1
            else:
                if ans==-1 or (arr[start] < arr[ans]):
                    ans = start
                start = mid+1
        return ans
        
