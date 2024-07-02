from typing import List
class Solution:

    def tabulationBottomUp(self, capacity:int, weights:List[int], values:List[int], n:int):
        dp = [[0]*(capacity+1) for i in range(n+1)]
        # dp[i][j] is telling me what is the largest value i can obtain when filling a knapsack with weights until i'th index of array and sack having capacity of j
        for i in range(n+1):
            for j in range(capacity+1):
                if i==0 or j==0:
                    # meaning either 0 elements of 0 capacity, the answer is 0
                    dp[i][j] = 0
                elif weights[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
        return dp[n][capacity]
    
    def recursive(self, capacity:int, weights:List[int], values:List[int], index:int, dp:List[List[int]]) -> int:
        if dp[index][capacity] != -1:
            return dp[index][capacity]
        
        if index==len(weights):
            return 0
        if capacity==0:
            return 0
        ans = -1
        if weights[index] > capacity:
            ans = self.recursive(capacity, weights, values, index+1, dp)
        else:
            ans = max(self.recursive(capacity, weights, values, index+1, dp), values[index] + self.recursive(capacity-weights[index], weights, values, index+1, dp))
        dp[index][capacity] = ans
        return ans
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W:int, wt:List[int], val:List[int], n:int):
        # code here
        # W = capacity. If it's 0 then I cannot get anything right
        # dp = [[-1]*(W+1) for i in range(n+1)]
        return self.tabulationBottomUp(W, wt, val, n)