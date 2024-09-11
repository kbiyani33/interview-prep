# TABLE METHOD OF 1D-DP(VERY FAMOUS)
from typing import List
class Solution:
    class Solution:
        def longestIncreasingSubsequence(self, n:int, arr):
            dp = [1]*n
            hashed = [i for i in range(n)]
            maxVal, last = -1, -1
            for i in range(n):
                for j in range(i):
                    if arr[i] > arr[j]:
                        if 1 + dp[j] > dp[i]:
                            hashed[i] = j
                            dp[i] = 1 + dp[j]
                if dp[i] > maxVal:
                    maxVal = dp[i]
                    last = i
            lis_arr = []
            lis_arr.append(arr[last])
            # print(last)
            while(last != hashed[last]):
                last = hashed[last]
                lis_arr.append(arr[last])
                
            # lis_arr.append(arr[last])   
            return lis_arr[::-1]
