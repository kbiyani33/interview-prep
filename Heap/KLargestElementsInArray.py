"""
Given an array [1, 23, 12, 9, 30, 2, 50] and an integer K, return the K largest elements.
Order of return doesn't matter.

Possible approaches ?
1. SORTING -> O(NlogN)
2. HEAP -> O(NlogK)
    Why heap ? Since for every value K < N, we are doing N-K extra work.


IDENTIFICATION ?
1. Array
2. K
3. Largest (So min heap)
"""

import heapq
from typing import List

def getKLargestElements(arr: List[int], K:int) -> List[int]:
    """
    Using functions directly
    """
    # return heapq.nsmallest(K, arr)
    op = []
    for i in arr:
        heapq.heappush(op, i)
        if len(op) > K:
            heapq.heappop(op)
    return op
# Please note we have 2 fun

if __name__=="__main__":
    arr = [7, 10, 4, 3, 20, 15]
    print(getKLargestElements(arr, K=3))
