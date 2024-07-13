from sys import *
from collections import *
from math import *

def lcs(s1:str, s2:str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s1[i]==s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

def lps(s:str):
    return lcs(s, s[::-1])

def minInsertion(s:str):
    # Write the function here.
    return len(s)-lps(s)
