from typing import List

def findNumberOfLIS(arr: List[int]) -> int:
    n = len(arr)

    # Initialize two dynamic programming lists for lengths and counts
    dp = [1] * n
    count = [1] * n

    maxi = 1

    for i in range(n):
        for prev_index in range(i):
            if arr[prev_index] < arr[i] and dp[prev_index] + 1 > dp[i]:
                dp[i] = dp[prev_index] + 1
                # Inherit the count
                count[i] = count[prev_index]
            elif arr[prev_index] < arr[i] and dp[prev_index] + 1 == dp[i]:
                # Increase the count
                count[i] += count[prev_index]
        
        maxi = max(maxi, dp[i])

    num_of_LIS = 0

    # Count the number of Longest Increasing Subsequences
    for i in range(n):
        if dp[i] == maxi:
            num_of_LIS += count[i]

    return num_of_LIS