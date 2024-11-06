from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
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
        
        MOD = 1000000007
        nseArr = nse(arr)
        preArr = pse(arr)

        ans = 0
        for i in range(len(arr)):
            ans = (ans%MOD + (arr[i] * (i-preArr[i]) * (nseArr[i] - i))%MOD)%MOD
        return ans