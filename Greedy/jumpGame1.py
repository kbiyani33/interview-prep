from typing import List

"""
Idea is that I need to be able to cross 0
I'll keep checking greedily if the maxIndexReachable is more than current index + val at current index

DRY Run
2,3 --> possible. No big deal (in first iteration only maxIndex reachable works fine)
2,1,0,4 --> not possible since max index never cross the index of 0 which is 2. 
            When the iteration reaches index 3(4) it'll see than curIndex is strictly more than maxindex(2). 
            So that's our flag to return false.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndexReachable = 0
        n = len(nums)
        target = n - 1

        for i in range(n):
            if i > maxIndexReachable:
                return False
            maxIndexReachable = max(maxIndexReachable, i+nums[i])
        return maxIndexReachable >= target
