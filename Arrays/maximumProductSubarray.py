from typing import List
import math

class Solution:
    def optimal(self, nums:List[int]):
        pref, suff = 1, 1
        maxPr = -math.inf
        n = len(nums)
        for i in range(n):
            if pref == 0: pref=1
            if suff == 0: suff=1

            pref *= nums[i]
            suff *= nums[n-1-i]
            maxPr = max(maxPr, pref, suff)
        return maxPr

    def better(self, nums:List[int]):
        maxPr = -math.inf
        n = len(nums)
        for i in range(n):
            pr = 1
            for j in range(i, n):
                pr *= nums[j]
                maxPr = max(maxPr, pr)
        return maxPr
    def brute(self, nums:List[int]):
        maxPr = -math.inf
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                currentPr = 1
                for k in range(i, j+1):
                    currentPr *= nums[k]
                maxPr = max(maxPr, currentPr)
        return maxPr
    def maxProduct(self, nums: List[int]) -> int:
        maxPr, n = -math.inf, len(nums)
        prefix, suffix = 1, 1
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-1-i]
            maxPr = max(maxPr, prefix, suffix)
            prefix = 1 if prefix==0 else prefix
            suffix = 1 if suffix==0 else suffix
        
        return maxPr