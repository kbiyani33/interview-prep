#User function Template for python3
import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        heap = []
        for i in range(K):
            heapq.heappush(heap, (arr[i][0], i, 0))
        result = []
        while(heap):
            val, arr_pos, val_pos = heapq.heappop(heap)
            result.append(val)
            
            if val_pos + 1 < len(arr[arr_pos]):
                heapq.heappush(heap, (arr[arr_pos][val_pos + 1], arr_pos, val_pos + 1))
        return result