"""
Given an unsorted array and two numbers x and k, find k closest values to x.
Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 . 

Suppose you have 5, 6, 7, 8, 9
When we needed K Largest elements, we had a heap of the array elements directly.

However, for K Closest values to input x, we will start subtracting x from each element and the heap is of the difference.

Now, next question is which heap ? 
We will need a max heap, since we want to store the smallest values and pop largest values, so max heap. 
Basically, smallest differences.
"""
from typing import List
import heapq
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # if x <= arr[0]:
    #     return arr[:k]
    # if x >= arr[-1]:
    #     return arr[(len(arr)-k):]
    # I need a max heap
    heap = []
    # diff_visited = {}
    for i in arr:
        heap_element = (-1 * abs(i-x), -1 * i)
        heapq.heappush(heap, heap_element)
        if len(heap) > k:
            heapq.heappop(heap)
    # print(heap)
    result = []
    for element in heap:
        heapq.heappush(result, -1 * element[-1])
    
    return sorted(result)