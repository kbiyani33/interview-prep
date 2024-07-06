from math import inf
from typing import List

class Solution:
    def tabulationBottomUpDP(self, N:int, capacity:int, val:List[int], wt:List[int]) -> int:
        # code here
        dp = [[0 for _ in range(capacity+1)] for _ in range(N+1)]
        for i in range(N-1, -1, -1):
            for j in range(1, capacity+1):
                notPick = dp[i+1][j]
                if wt[i] > j:
                    dp[i][j] = notPick
                else:
                    pick = val[i] + dp[i][j-wt[i]] # index is the same since i have infinite supply
                    dp[i][j] = max(pick, notPick)
        return dp[0][capacity]

    def recursive(self, N:int, capacity:int, val:List[int], wt:List[int], index:int, dp:List[List[int]]):
        
        if capacity==0 or index==N: return 0
        
        if dp[index][capacity] != -1:
            return dp[index][capacity] 
        
        notPick = self.recursive(N, capacity, val, wt, index+1, dp)
        if wt[index] > capacity:
            ans = notPick
        else:
            pick = val[index] + self.recursive(N, capacity-wt[index], val, wt, index, dp)
            ans = max(pick, notPick)
        dp[index][capacity] = ans
        return ans
        
    def knapSack(self, N, capacity, val, wt):
        # code here
        dp = [[-1 for _ in range(capacity+1)] for _ in range(N+1)]
        return self.recursive(N, capacity, val, wt, 0, dp)