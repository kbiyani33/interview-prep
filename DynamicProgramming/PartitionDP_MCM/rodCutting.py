from os import *
from sys import *
from collections import *
from math import *

from typing import List

def recursiveCostOfCutting(cuts:List[int], i:int, j:int, dp:List[List[int]]):
    if i>j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    minI = inf
    for index in range(i, j+1):
        ans = cuts[j+1] - cuts[i-1] + recursiveCostOfCutting(cuts, i, index-1, dp) + recursiveCostOfCutting(cuts, index+1, j, dp)
        minI = min(minI, ans)
    dp[i][j] = minI
    return minI

def tabulationBottomUpDP(n:int, c:int, cuts:List[int]) -> int:
    cuts = [0] + cuts + [n]
    cuts.sort()

    dp = [[0]*(c+2) for i in range(c+2)]
    for i in range(c, 0, -1):
        for j in range(1, c+1):
            if i>j: continue
            minI = inf
            for index in range(i, j+1):
                ans = cuts[j+1]-cuts[i-1] + dp[i][index-1] + dp[index+1][j]
                minI = min(minI, ans)
            dp[i][j] = minI
    return dp[1][c]

def cost(n: int, c: int, cuts: List[int]) -> int:
    # Write your code here.
    # n = length to be cut
    # c = number of elements in cuts array(not needed tbh)
    # cuts = possible cuts
    # cuts = [0] + cuts + [n]
    # Why have we added this ? Because before any cut, we want to get the cost which is the initial length of the portion being cut
    # We will now sort this, to ensure that we can independently call the left and right partitions
    # cuts.sort()
    # Now we will run the recursive call. How ? We will start by taking the first cut to be from 1st element of cuts and then run
    # dp = [[-1]*(c+1) for i in range(c+1)]
    # return recursiveCostOfCutting(cuts=cuts, i=1, j=c, dp=dp)
    return tabulationBottomUpDP(n,c,cuts)

    