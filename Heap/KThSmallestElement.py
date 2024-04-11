"""
Given an array and a number k where k is smaller than size of array, we need to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.

Example:
Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7

Make a max heap and make sure that the size of heap is never greater than K.
Everytime we go above K elements in the max heap, remove the top and it'll again go back to K.

"""

from typing import List
import heapq

def getKthSmallestElement(arr:List[int], K:int) -> int:
    # return heapq.nsmallest(K, arr)[-1]
    maxHeapElements = [-1 * i for i in arr]
    heap = []

    for i in maxHeapElements:
        heapq.heappush(heap, i)
        if len(heap) > K:
            heapq.heappop(heap)
    
    # print(heap)
    return heap[0] * -1

if __name__=="__main__":
    arr = [7, 10, 4, 3, 20, 15]
    print(getKthSmallestElement(arr, K=3))

