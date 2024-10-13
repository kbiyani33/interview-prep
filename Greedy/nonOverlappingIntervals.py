from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        counter = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                counter += 1
            else:
                prev = curr
        return counter