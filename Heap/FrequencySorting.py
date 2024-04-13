from typing import List
from collections import Counter
import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        heap = []
        for key in count:
            element = (count[key], -1*key)
            heapq.heappush(heap, element)
        result = []
        while(heap):
            element = heapq.heappop(heap)
            result += [-1*element[1]]*(element[0])
        return result