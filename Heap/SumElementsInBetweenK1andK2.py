"""
Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two k1’th and k2’th smallest elements of the array. It may  be assumed that all elements of array are distinct.

Example :
Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6  
Output : 26          
         3rd smallest element is 10. 6th smallest element 
         is 20. Sum of all element between k1 & k2 is
         12 + 14 = 26 . 
"""

import heapq
from typing import List

def getKthSmallestElement(arr: List[int], K:int) -> int:
    heap = []
    for i in arr:
        heapq.heappush(heap, -1 * i)
        if len(heap) > K:
            heapq.heappop(heap)
    return -1 * heapq.heappop(heap)

if __name__=="__main__":
    arr = [20, 8, 22, 4, 12, 10, 14]
    k1 = 3
    k2 = 6
    k1_val = getKthSmallestElement(arr, k1)
    k2_val = getKthSmallestElement(arr, k2)
    total = 0
    for i in arr:
        if i > k1_val and i <k2_val:
            total += i
    print(total)
