"""
Problem Statement:
You are given an integer array nums sorted in ascending order, and an integer target. Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). You must write an algorithm with O(log n) runtime complexity that returns the index of target if it is in nums, or -1 if it is not in nums.

Identification:
	•	The array was originally sorted but then rotated, which is a scenario where binary search can still be utilized.
	•	The problem asks for specific element retrieval with logarithmic time complexity, suggesting that binary search could be modified for this purpose.


Brute Force Solution:
	•	Traverse the array from start to end and check if the current element is the target.
	•	Time Complexity: O(n)

Algorithm
    Initialize left and right pointers at the beginning and end of the array, respectively.
    Use binary search (while left <= right) to continuously narrow down the search range until the target is found or the search range is exhausted.
    At each iteration (mid), compare the target value with the middle element:
    If nums[mid] == target, return mid as the index of the target.
    Check the rotation point of the array to determine which half of the array (left or right of mid) to search next:
    If nums[mid] >= nums[left] (the left half is sorted):
    Check if target is within the sorted left half (nums[left] <= target < nums[mid]).
    Adjust the search range (right = mid - 1 or left = mid + 1) based on the comparison result.
    If nums[mid] < nums[right] (the right half is sorted):
    Check if target is within the sorted right half (nums[mid] < target <= nums[right]).
    Adjust the search range (left = mid + 1 or right = mid - 1) based on the comparison result.

"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
            # identify the sorted portion
            if nums[mid]<nums[end]:
                if nums[mid]<target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
                
        return -1
        