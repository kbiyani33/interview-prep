from typing import List
# sorting is necessary since I am only gonna compare the divisibility with the previous one. If that's divisible, everyone before that are also divisible
def divisibleSet(arr: List[int]) -> List[int]:
    # write your code here
    n = len(arr)
    arr.sort() # sorting is necessary since I am only gonna compare the divisibility with the previous one. If that's divisible, everyone before that are also divisible
    dp = [1]*n
    maxLen, hashed, lastIndex = -1, [-1]*n, -1
    for i in range(n):
        hashed[i] = i
        for prev in range(i):
            if (arr[i]%arr[prev] == 0) and (dp[i] < 1 + dp[prev]):
                dp[i] = 1 + dp[prev]
                hashed[i] = prev
        if dp[i] > maxLen:
            maxLen = dp[i]
            lastIndex = i
    
    divisibleSubset = []
    divisibleSubset.append(arr[lastIndex])
    while hashed[lastIndex] != lastIndex:
        lastIndex = hashed[lastIndex]
        divisibleSubset.append(arr[lastIndex])
    # print(divisibleSubset)
    return divisibleSubset