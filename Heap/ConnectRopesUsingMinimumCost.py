#User function Template for python3
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        if n == 2:
            return sum(arr)
        if n == 1:
            return 0
        
        heap = []
        for i in arr:
            heapq.heappush(heap, i)
        totalCost = 0
        # print(heap)
        while(heap):
            if len(heap)==1:
                break
            min1 = heapq.heappop(heap)
            min2 = heapq.heappop(heap)
            totalCost += min1 + min2
            heapq.heappush(heap, min1+min2)
        return totalCost