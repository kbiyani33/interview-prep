from typing import List

def lengthOfLIS(arr: List[int]) -> int:
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return dp

def longestBitonicSubsequence(arr: List[int], n: int) -> int:
    # write your code here
    lis_front = lengthOfLIS(arr)
    lis_back = lengthOfLIS(arr[::-1])[::-1]

    maxI = -1
    for i in range(n):
        bitonic = lis_front[i] + lis_back[i] - 1
        maxI = max(maxI, bitonic)
    return maxI