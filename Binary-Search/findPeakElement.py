"""
Question 2: Find Peak Element

Problem Statement:
A peak element in an array is an element that is strictly greater than its neighbors. Given an input array nums, where nums[i] ≠ nums[i + 1] for all valid i, find a peak element and return its index. The array may contain multiple peaks, in that case, return the index to any of the peaks.

Identification:
	•	The problem involves finding a local maximum, which hints at a possible binary search approach.
	•	It's not about sorting or searching for a specific value, which is a non-traditional application of binary search.


Brute Force Solution:
	•	Iterate through the array comparing each element to its neighbors.
	•	Time Complexity: O(n)


Binary Search Improvement:
	•	Use binary search to find any peak.
	•	If the middle element is not a peak, move towards the side with the larger neighbor.
	•	Time Complexity: O(log n)


Dry Run:
Given array: [1, 2, 3, 1]
	•	Start with low = 0, high = 3
	•	mid = (0 + 3) // 2 = 1, element at mid is 2
	•	Compare to neighbors: 2 > 1 (left neighbor) but 2 < 3 (right neighbor)
	•	Since the right neighbor is greater, move right: low = mid + 1
	•	Now low = 2, high = 3
	•	mid = (2 + 3) // 2 = 2, element at mid is 3
	•	Compare to neighbors: 3 > 2 (left neighbor) and 3 > 1 (right neighbor)
	•	Element at mid is a peak, return index 2.


Corner Cases:
	•	Array has only one element, which is the peak.
	•	Peak is at the first or last index of the array.
"""
import math
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums)-1
        while(start<end):
            middle = start + (end-start)//2
            if nums[middle+1] > nums[middle]:
                start = middle+1
            else:
                end = middle
        return start