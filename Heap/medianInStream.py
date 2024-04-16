import heapq
"""
Algorithm - 
small = max heap
large = min heap

Insert to small
Then insert top of small to large
if len(large) becomes greater than small then insert top of large back to small

Median is top of small if len of small and large different else average of top of small and large
"""
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