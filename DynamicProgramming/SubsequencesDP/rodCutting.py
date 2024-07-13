from math import inf
from typing import List

class Solution:
    def recursive(self, price:List[int], n:int, index:int) -> int:
        if n==0:
            return 0
        if index>=n:
            return -inf
        
        cutLength = index+1
        cutPrice = price[index]

        # We always have the option to not take this cutLength
        notTake = self.recursive(price, n, index+1)
        # We can have this cutLenght if our remaining length(n) is greater than or equal to cutLength
        if n >= cutLength:
            take = cutPrice + self.recursive(price, n-cutLength, index) # We can still try same cutLength
            return max(take, notTake)
        return notTake
    
    def memoizedDP(self, price:List[int], n:int, index:int, dp:List[List[int]]) -> int:
        if n==0:
            return 0
        
        if index>=n:
            return -inf
        
        if dp[index][n] != -inf:
            return dp[index][n]
        
        cutLength = index+1
        cutPrice = price[index]

        # We always have the option to not take this cutLength
        ans = -1
        notTake = self.memoizedDP(price, n, index+1, dp)
        # We can have this cutLenght if our remaining length(n) is greater than or equal to cutLength
        if n >= cutLength:
            take = cutPrice + self.memoizedDP(price, n-cutLength, index, dp) # We can still try same cutLength
            ans = max(take, notTake)
        else:
            ans = notTake
        dp[index][n] = ans
        return ans


    def cutRod(self, price:List[int], n:int) -> int:
        #code here
        dp = [[-inf for _ in range(n+1)] for _ in range(n+1)]
        return self.memoizedDP(price, n, 0, dp)
    
    def tabulationDPBottomUp(self, price:List[int], n:int) -> int:
        dp = [[-inf for _ in range(n+1)] for _ in range(n+1)]
        # For n(j) = 0 I will get only 0 value, so that's 0
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(1, n+1):
                cutLength = i+1
                cutPrice = price[i]

                notTake = dp[i+1][j]
                if j>=cutLength:
                    take = cutPrice + dp[i][j-cutLength]
                    ans = max(take, notTake)
                else:
                    ans = notTake
                dp[i][j] = ans
        return dp[0][n]