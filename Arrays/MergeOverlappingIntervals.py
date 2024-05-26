from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()
        ans = []
        for interval in intervals:
            if len(ans)==0 or interval[0]>ans[-1][1]:
                ans.append(interval)
                continue
            lastAnsInterval = ans[-1]
            lastAnsInterval[0] = min(interval[0], lastAnsInterval[0])
            lastAnsInterval[1] = max(interval[1], lastAnsInterval[1])

        return ans