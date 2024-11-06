from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        # nums.extend(nums[:])
        n = len(nums)

        nge = [-1 for _ in range(n)]
        stack = [nums[n-1]]
        for i in range(2*n - 2, -1, -1):
            idx = i%n
            topOfStack = stack[-1]
            if nums[idx] < topOfStack:
                nge[idx] = topOfStack
            else:
                while stack and stack[-1] <= nums[idx]:
                    stack.pop()
                if stack: nge[idx] = stack[-1]
            stack.append(nums[idx])
        return nge
