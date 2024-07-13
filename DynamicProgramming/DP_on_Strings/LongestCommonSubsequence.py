"""
given 2 string, return length of longest common subsequence

first   = abcdgh
second  = abedfh

LCS = abdh thus we return 4

What's the base condition
if even one of the strings has a length 0 then it's no point, return 0
"""

import time

def lcs_dp(first:str, second:str) -> int:
    m = len(first)
    n = len(second)

    dp = [[None] * (n+1) for i in range(m+1)]
    """
    What is dp[m][n] referring to exactly ??
    It means that what's the answer of LCS output string length when we take only 
    first m and 
    first n 
    letters from first and second input string respectively.
    so dp[0][0] is LCS int with 0 letters in both first and last
    """
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif first[i-1] == second[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


def recursiveLCS(first:str, second:str) -> int:

    if len(first) == 0 or len(second) == 0:
        return 0
    
    lastchar1 = first[-1]
    lastchar2 = second[-1]

    if lastchar1 == lastchar2:
        return 1+recursiveLCS(first[:-1], second[:-1])
    else:
        return max(recursiveLCS(first, second[:-1]), recursiveLCS(first[:-1], second))


if __name__ == "__main__":
    first = "abcdgf"
    second = "abdeghr"
    # print(recursiveLCS(first, second))
    start1 = time.time()
    print(recursiveLCS(first, second))
    end1 = time.time()

    print("recursive time is " + str(end1-start1))

    start2 = time.time()
    op = lcs_dp(first, second)
    print(op)
    end2 = time.time()
    print("DP time is " + str(end2-start2))


# CODE STUDIO code below(coding ninjas/naukri)

from sys import stdin

def recursive_lcs(s, t, i1, i2, dp):
    if i1==len(s) or i2==len(t):
        return 0
    
    if dp[i1][i2] != -1:
        return dp[i1][i2]
    
    if s[i1] == t[i2]:
        ans = 1 + recursive_lcs(s, t, i1+1, i2+1, dp)
    else:
        ans = max(recursive_lcs(s, t, i1, i2+1, dp), recursive_lcs(s, t, i1+1, i2, dp))

    dp[i1][i2] = ans
    return ans

def tabulationDp_BottomUp(s, t):
    m, n = len(s), len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # I need to return dp[0][0] so i'll move backwards
    for i1 in range(m-1, -1, -1):
        for i2 in range(n-1, -1, -1):
            if s[i1]==t[i2]:
                dp[i1][i2] = 1 + dp[i1+1][i2+1]
            else:
                dp[i1][i2] = max(dp[i1][i2+1], dp[i1+1][i2])
    return dp[0][0]

def lcs(s, t) :
    # m, n = len(s), len(t)
    # dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
    # return recursive_lcs(s, t, 0, 0, dp)
    return tabulationDp_BottomUp(s, t)

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
    while i<m:
        sqs += s[i]
        i += 1
    while j<n:
        sqs += t[j]
        j += 1
    return sqs