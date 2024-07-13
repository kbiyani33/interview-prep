from os import *
from sys import *
from collections import *
from math import *
from typing import List

class Solution:
    def tabulation(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        # if amount(j) needed is 0 there is 1 way to not take any coins since only non 0 denominations are there
        for i in range(n+1):
            dp[i][0] = 1
        # for 0 coins, and non 0 amount, we cannot have any way thus 0 which is already initialized

        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                notTake, ans = dp[i+1][j], -1
                if coins[i] > j:
                    ans = notTake
                else:
                    ans = notTake + dp[i][j-coins[i]]
                dp[i][j] = ans
        return dp[0][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        def recursive(coins, amount, index, dp):
            if amount==0:
                return 1
            if index==len(coins):
                return 0
            if dp[index][amount] != -1:
                return dp[index][amount]

            ans = -1
            notTake = recursive(coins, amount, index+1, dp)
            if coins[index] > amount:
                ans = notTake
            else:
                take = recursive(coins, amount-coins[index], index, dp)
                ans = take+notTake
            dp[index][amount] = ans
            return ans
        m, n = len(coins), amount
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return recursive(coins, amount, 0, dp)
            
