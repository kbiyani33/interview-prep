"""
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Example:
Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

What is meaning of K Sorted or Nearly Sorted ?
Any value is at most K positions away from the right position.

Basically, for every index i in the input array, the right position can be i-k <= i <= i+k


Worst case --> Sort it and give O(NlogN)

IDENTIFICATION
1. Array
2. K
3. sorted(at most k positions away, so min heap)
"""

import heapq
from typing import List
def nearlySorted(a:List[int], k:int):
    # code here
    """
    Make min heap and keep pushing elements. 
    Its said that any element is at most k positions away from right position.
    """
    op = []
    heap = []
    for i in a:
        heapq.heappush(heap, i)
        if len(heap) > k: # then the top is definitely minimum in current elements
            op.append(heapq.heappop(heap))
    for j in range(len(heap)):
        op.append(heapq.heappop(heap))
    # print(heap)
    return op

if __name__=="__main__":
    arr = [7, 10, 4, 3, 20, 15]
    print(nearlySorted(arr, K=3))
