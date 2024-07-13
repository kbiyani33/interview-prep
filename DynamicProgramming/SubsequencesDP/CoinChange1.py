from os import *
from sys import *
from collections import *
from math import *
from typing import List

class Solution:
    def tabulationDP(self, coins:List[int], amount:int) -> int:
        n = len(coins)
        dp = [[inf for _ in range(amount+1)] for _ in range(n+1)]
        # number of coins needed to get 0 amount is 0
        for i in range(n+1):
            dp[i][0] = 0
        
        # from 0 coins, number of ways to make non zero amount is inf which is already done in the initialization
        # now, I will go in the reverse direction of my result as per my recursive code
        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                notTake, ans = dp[i+1][j], -1
                if coins[i] > j:
                    ans = notTake
                else:
                    take = 1 + dp[i][j-coins[i]]
                    ans = min(take, notTake)
                dp[i][j] = ans
        return dp[0][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:

        def recursive(coins, amount, index, dp):
            if amount==0:
                return 0
            if index==len(coins):
                return inf
            if dp[index][amount] != -inf:
                return dp[index][amount]

            notTake = recursive(coins, amount, index+1, dp)
            ans = -1
            if coins[index] > amount:
                # I will never use this
                ans = notTake
            else:
                take = 1+recursive(coins, amount-coins[index], index, dp)
                ans = min(take, notTake)
            
            
            dp[index][amount] = ans
            return dp[index][amount]

        dp = [[-inf for _ in range(amount+1)] for _ in range(len(coins)+1)]
        ans = recursive(coins, amount, 0, dp)
        if ans==inf:
            return -1
        return ans

        
        