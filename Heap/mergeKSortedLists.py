import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, k):
        # code here
        # return merged list
        if k==1:
            return arr[0]
        minHeap = []
        for i in range(k):
            heapq.heappush(minHeap, (arr[i][0], i, 0))
        
        result = []
        while minHeap:
            val, arrIndex, elementIndex = heapq.heappop(minHeap)
            result.append(val)
            if elementIndex < k-1:
                heapq.heappush(minHeap, (arr[arrIndex][elementIndex+1], arrIndex, elementIndex+1))
        
        return result