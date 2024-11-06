from typing import List
from math import inf

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -inf
        stack = []
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                # nse of element = i
                # pse of element = the top of stack right now
                pse = -1
                if stack:
                    pse = stack[-1]
                maxArea = max(maxArea, (i-pse-1)*heights[element])
            stack.append(i)
        while stack:
            element = stack.pop()
            pse = stack[-1] if stack else -1
            maxArea = max(maxArea, (n - pse - 1)*heights[element])
        return maxArea
        