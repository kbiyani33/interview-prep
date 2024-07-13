from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        maxInPiles = max(piles)
        low, high = 1, maxInPiles
        if n==h:
            return maxInPiles
        low, high = 1, maxInPiles
        def getTimeToFinishUsingThisK(k):
            ans = 0
            for i in range(n):
                ans += ceil(piles[i]/k)
            return ans

        while low<=high:
            mid = low + (high-low)//2
            # Let mid be the answer
            hoursNeeded = getTimeToFinishUsingThisK(mid)
            if hoursNeeded <= h:
                high = mid-1
            else:
                low = mid+1
        return low