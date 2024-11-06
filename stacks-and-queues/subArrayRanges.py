# from typing import List
from typing import List

class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        def nge(arr):
            n = len(arr)
            result = [n for _ in range(n)]
            stack = [n-1]
            for i in range(n-2, -1, -1):
                top = stack[-1]
                if arr[top] > arr[i]:
                    result[i] = top
                else:
                    while stack and arr[stack[-1]] <= arr[i]:
                        stack.pop()
                    if stack: result[i] = stack[-1]
                stack.append(i)
            return result
        def nse(arr):
            n = len(arr)
            result = [n for _ in range(n)]
            stack = [n-1]
            for i in range(n-2, -1, -1):
                top = stack[-1]
                if arr[top] < arr[i]:
                    result[i] = top
                else:
                    while stack and arr[stack[-1]] >= arr[i]:
                        stack.pop()
                    if stack: result[i] = stack[-1]
                stack.append(i)
            return result

        def pse(arr):
            n = len(arr)
            result = [-1 for _ in range(n)]
            stack = [0]
            for i in range(1, n):
                top = stack[-1]
                if arr[top] <= arr[i]:
                    result[i] = top
                else:
                    while stack and arr[stack[-1]] > arr[i]:
                        stack.pop()
                    if stack: result[i] = stack[-1]
                stack.append(i)
            return result

        def pge(arr):
            n = len(arr)
            result = [-1 for _ in range(n)]
            stack = [0]
            for i in range(1, n):
                top = stack[-1]
                if arr[top] >= arr[i]:
                    result[i] = top
                else:
                    while stack and arr[stack[-1]] < arr[i]:
                        stack.pop()
                    if stack: result[i] = stack[-1]
                stack.append(i)
            return result       
        nseArr = nse(arr)
        ngeArr = nge(arr)
        pseArr = pse(arr)
        pgeArr = pge(arr)

        ans = 0
        for i in range(len(arr)):
            ans += arr[i] * (i-pgeArr[i])*(ngeArr[i] - i)
            ans -= arr[i] * (i-pseArr[i])*(nseArr[i] - i)
        return ans