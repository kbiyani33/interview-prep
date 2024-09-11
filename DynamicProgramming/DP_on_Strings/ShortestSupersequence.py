"""
The idea in getting length is simple

The idea in getting the string is as follows

We traverse the LCS DP Matrix in the same way. however, we simply used to move in the direction of max(dp[i-1][j], dp[i][j-1]) earlier.
For supersequence, we will include that character as well.

And we will run loop again until both i and j become 0
"""
from typing import List

def getlcs(first:str, second:str) -> List[List[int]]:

    m = len(first)
    n = len(second)

    dp = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            elif first[i-1] == second[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def length_shortest_common_supersequence(first:str, second:str):
    dp_lcs = getlcs(first, second)
    return len(first) + len(second) - dp_lcs[-1][-1]

from sys import *
from collections import *
from math import *

def shortestSupersequence(s: str, t: str) -> str:
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # I need to return dp[0][0] so i'll move backwards
    for i1 in range(m-1, -1, -1):
        for i2 in range(n-1, -1, -1):
            if s[i1]==t[i2]:
                dp[i1][i2] = 1 + dp[i1+1][i2+1]
            else:
                dp[i1][i2] = max(dp[i1][i2+1], dp[i1+1][i2])
    
    sqs = ""
    i, j = 0, 0
    while i < m and j < n:
        if s[i]==t[j]:
            sqs += s[i]
            i += 1
            j += 1
            continue
        
        if dp[i+1][j] > dp[i][j+1]:
            sqs += s[i]
            i += 1
        else:
            sqs += t[j]
            j += 1
    while j<n:
        sqs += t[j]
        j += 1
    while i<m:
        sqs += s[i]
        i += 1
    
    return sqs