from bisect import bisect_left
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_Array = []
        for i in nums:
            if len(lis_Array) == 0 or i > lis_Array[-1]:
                lis_Array.append(i)
            else:
                left_bound = bisect_left(lis_Array, i)
                lis_Array[left_bound] = i
        # print(lis_Array)
        return len(lis_Array)

        