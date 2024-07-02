from os import *
from sys import *
from collections import *
from math import *

from typing import List

def recursiveMaxCoins(a:List[int], i:int, j:int, dp:List[List[int]]):
    if i>j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    maxI = -inf
    for index in range(i, j+1):
        # index means that this is the last one I am gonna pick out
        ans = a[i-1]*a[index]*a[j+1] + recursiveMaxCoins(a, i, index-1, dp) + recursiveMaxCoins(a, index+1, j, dp)
        # Now index has been removed so next and previous might change accordingly.
        maxI = max(maxI, ans)
    dp[i][j] = maxI
    return maxI

def tabulationBottomUpDP(a:List[int]) -> int:
    n = len(a)
    a = [1] + a + [1]
    dp = [[0]*(n+2) for i in range(n+2)]
    for i in range(n, 0, -1):
        for j in range(1, n+1):
            if i>j:
                continue
            maxI = -inf
            for index in range(i, j+1):
                ans = a[i-1]*a[index]*a[j+1] + dp[i][index-1] + dp[index+1][j]
                maxI = max(maxI, ans)
            dp[i][j] = maxI
    return dp[1][n]



def maxCoins(a: List[int]) -> int:
	# Write your code here.
    # n = len(a)
    # a = [1] + a + [1]
    # dp = [[-1]*(n+1) for i in range(n+1)]
    # return recursiveMaxCoins(a, 1, n, dp)
    return tabulationBottomUpDP(a)