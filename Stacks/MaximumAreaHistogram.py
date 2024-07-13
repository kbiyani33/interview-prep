from math import inf
from collections import deque
from typing import List

class Solution:
    def getNearestSmallerElementIndexRight(self, histogram:List[int], n:int) -> List[int]:
        result, stack = deque(), deque()
        
        for i in range(n-1, -1, -1):
            while(len(stack) > 0 and histogram[stack[-1]] >= histogram[i]):
                stack.pop()
                
            pg = n if len(stack)==0 else stack[-1]
            result.appendleft(pg)
            
            stack.append(i)
        return list(result)
            
            
    def getNearestSmallerElementIndexLeft(self, histogram:List[int], n:int) -> List[int]:
        result, stack = deque(), deque()
        
        for i in range(n):
            while(len(stack) > 0 and histogram[stack[-1]] >= histogram[i]):
                stack.pop()
            pg = -1 if len(stack) == 0 else stack[-1]
            result.append(pg)
            stack.append(i)
        
        return list(result)
        
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        """
        What's the idea ??
        for each element at index i, find nearest smallest element on left and nearest smallest element on right
        The area for this rectangle is arr[i]*(i-(nsl+1)) + arr[i]*((nsr-1)-i)
        """
        maxHistArea = -inf
        n = len(histogram)
        leftSmallest = self.getNearestSmallerElementIndexLeft(histogram, n)
        rightSmallest = self.getNearestSmallerElementIndexRight(histogram, n)
        
        # print("left ", leftSmallest)
        # print("right ", rightSmallest)
        left = leftSmallest
        right = rightSmallest
        for i in range(n):
            currentArea = histogram[i] * (right[i] - (left[i] + 1))
            maxHistArea = max(maxHistArea, currentArea)
            
        
        return maxHistArea
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxA = [], -inf
        n = len(heights)
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                top = stack.pop()
                height = heights[top]
                width = 0
                if stack:
                    width = (i-stack[-1]-1)
                else:
                    width = i
                maxA = max(maxA, width*height)
            stack.append(i)
        return maxA

        