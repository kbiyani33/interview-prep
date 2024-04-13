"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
from typing import List
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if k >= len(nums):
        return nums
    
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    heap = []
    for i in freq:
        heapq.heappush(heap, (freq[i], i))
        if len(heap) > k:
            heapq.heappop(heap)
    
    op = []
    for element in heap:
        op.append(element[-1])
    return op