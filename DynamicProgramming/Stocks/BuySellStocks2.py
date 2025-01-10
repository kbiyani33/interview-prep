from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def tabulationBottomUp(prices:List[int]) -> int:
            n = len(prices)
            dp = [[-inf for _ in range(2)] for _ in range(n+1)]

            # fixing the base conditions
            # when holding is false, then I'll have to make the dp value as 0
            dp[n][int(False)] = 0
            for i in range(n-1, -1 -1):
                for j in range(2):
                    if j==int(False):
                        dp[i][j] = max(dp[i+1][j], dp[i+1, int(True)]-prices[i])
                    else:
                        dp[i][j] = max(prices[i] + dp[i+1][int(False)], dp[i+1][j])
            return dp[0][int(False)]



        def recursive(prices:List[int], index:int, holding:bool, dp:List[List[int]]) -> int:
            if index == len(prices):
                # I am going out of the loop
                # If I am not holding any stock, then profit will be 0 for this case
                # otherwise it'll be -inf since i never want to enter this state :)
                if holding:
                    return -inf
                return 0
            if dp[index][int(holding)] != -1:
                return dp[index][int(holding)]
            # now I am going to see the following possible cases
            """
            1. If I am not holding, then I may or may not buy it here
            2. If I am holding, I'll check if current price is actually greater than prevBuying price only then it'll make sense to even attemp to sell here
            """
            ans = -1
            if not holding:
                # I have an option to buy and move ahead or don't buy at all
                a1 = recursive(prices, index+1, holding, dp)
                a2 = recursive(prices, index+1, True, dp) - prices[index]
                ans = max(a1, a2)
            else:
                # I have an option to just sell today. I may sell today or I may not
                a1 = prices[index] + recursive(prices, index+1, False, dp)
                a2 = recursive(prices, index+1, holding, dp)
                ans = max(a1, a2)
            dp[index][int(holding)] = ans
            return ans

        # len(price)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return recursive(prices, 0, False, dp)
        