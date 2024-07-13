from os import *
from sys import *
from collections import *
from math import *
from typing import List

import sys
sys.setrecursionlimit(10**7)

from typing import List
def recursiveSolution(grid:List[List[int]], cr:int, cc:int, dp:List[List[int]])->int:
    m, n = len(grid), len(grid[0])
    if cr==m-1 and cc==n-1:
        return grid[cr][cc]
    if cr==m or cc==n:
        return inf
    if dp[cr][cc] != inf:
        return dp[cr][cc]
    # either move right or move down and get the minimum ans
    rightAns = recursiveSolution(grid, cr, cc+1, dp)
    downAns = recursiveSolution(grid, cr+1, cc, dp)
    dp[cr][cc] = grid[cr][cc]+min(rightAns, downAns)
    return dp[cr][cc]

def minSumPath(grid:List[List[int]]):
    # Write your code here.
    m, n = len(grid), len(grid[0])
    dp = [[inf]*(n+1) for i in range(m+1)]
    return recursiveSolution(grid, 0, 0, dp)

def tabulationBottomUpDP(grid):
    m, n = len(grid), len(grid[0])
    dp = [[inf]*(n+1) for i in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            ans = grid[i][j]
            if not (i==m-1 and j==n-1):
                ans += min(dp[i][j+1], dp[i+1][j])
            dp[i][j] = ans
    return dp[0][0]


# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1