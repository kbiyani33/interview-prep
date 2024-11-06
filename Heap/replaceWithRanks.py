"""
Main idea is that the position is going to be equal to the position it was obtained at.
The only tricky thing is for repeated values.
For that we don't need any visited set/array. We only care about the previous element.
If the previous element is different from current element, then great, we will increase positoin and move ahead.
Otherwise position remains the same as previous.
Since it's minheap, 2 or more equal element will be popped one after another :)
"""
import heapq
class Solution:
    def replaceWithRank(self, N, arr):
        # Code here
        minHeap = []
        for i in range(N):
            heapq.heappush(minHeap, (arr[i], i))
        ranks = [-1 for _ in range(N)]
        prev = -1
        position = 0
        while minHeap:
            element, index = heapq.heappop(minHeap)
            if element != prev:
                position += 1
                prev = element
            ranks[index] = position
        return ranks