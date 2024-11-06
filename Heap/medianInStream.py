import heapq
from heapq import *
"""
Algorithm - 
small = max heap
large = min heap

Insert to small
Then insert top of small to large
if len(large) becomes greater than small then insert top of large back to small

Median is top of small if len of small and large different else average of top of small and large
"""

class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        left, right = self.leftMaxHeap, self.rightMinHeap
        # step 1 is to add it to max heap
        heappush(left, -num)
        # check if max of maxHeap is < min of minHeap
        if left and right and -1 * left[0] > right[0]:
            element = heappop(left) * -1
            heappush(right, element)
        # check if size differences if greater than 1
        if len(left) > len(right) + 1:
            element = heappop(left) * -1
            heappush(right, element)
        # ensuring left has equal or more elements than right
        if len(right) > len(left):
            element = heappop(right)
            heappush(left, -element)

    def findMedian(self) -> float:
        
        if self.size % 2 == 1:
            return self.leftMaxHeap[0] * -1
        #     if len(self.leftMaxHeap) > len(self.rightMinHeap):
        #         return self.leftMaxHeap[0] * -1
        #     return self.rightMinHeap[0]
        else:
            return (self.leftMaxHeap[0] * -1 + self.rightMinHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class Solution:
    small, large = [], []
    def __init__(self):
        self.small = []
        self.large = []
        
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        small = self.small
        large = self.large
        heapq.heappush(large, -1 * heapq.heappop(small))
        
        if len(large) > len(small):
            heapq.heappush(small, -1 * heapq.heappop(large))
            
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        small = self.small
        large = self.large
        
        if len(small) > len(large):
            return -1 * small[0]
        else:
            return (-1 * small[0] + large[0])/2
        
        
        
        
    def insertHeaps(self,x:int):
        #:param x: value to be inserted
        #:return: None
        # code here
        small = self.small
        heapq.heappush(small, -x)
        self.balanceHeaps()