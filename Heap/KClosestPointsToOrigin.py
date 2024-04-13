from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        heap = []
        for point in points:
            x, y = point[0], point[1]
            distance = x**2 + y**2
            heap_element = (-1*distance, point)
            heapq.heappush(heap, heap_element)

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in heap:
            result.append(i[-1])
        return result