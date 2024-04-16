#User function Template for python3
"""
Enhanced Breakdown
Initialization:

Count the frequency of each character in the string.
Populate the max heap with these frequencies.
Processing Each Character:

Pop the top two characters from the max heap (i.e., the ones with the highest frequency).
Append these two characters to the result string.
Decrement their frequencies and re-insert them back into the max heap.
If only one character remains in the heap, make sure it doesn't exceed half of the string length, otherwise, return an empty string.
Wrap-up:

If there's a single remaining character with a frequency of 1, append it to the result.
Join all the characters to return the final reorganized string.
"""
from collections import Counter
import heapq
class Solution :
    def rearrangeString(self, s:str):
        heap = []
        freq = Counter(s)
        for key in freq:
            heapq.heappush(heap, tuple([-1 * freq[key], key]))
        result = ""
        # print(heap)
        while(len(heap) > 1):
            top1, s1 = heapq.heappop(heap)
            # print(heap)
            top2, s2 = heapq.heappop(heap)
            result = result + s1 + s2
            if -top1 >= 2:
                heapq.heappush(heap, (top1+1, s1))
            if -top2 >= 2:
                heapq.heappush(heap, (top2+1, s2))
        # print(heap)
        if len(heap) == 1:
            top, s = heapq.heappop(heap)
            if -top > 1:
                return ""
            result += s
        return result