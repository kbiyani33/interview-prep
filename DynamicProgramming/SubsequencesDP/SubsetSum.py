class Solution:
    def recursive(self, arr, sum, index, dp):
        if index==len(arr) and sum>0: # This sum>0 is important, since it's possible that the sum needed is actually 0 which is possible i empty subset
            return False
        if sum==0:
            return True
        if dp[index][sum] != -1:
            return dp[index][sum]
        
        if arr[index] > sum:
            ans = self.recursive(arr, sum, index+1, dp)
        else:
            ans = self.recursive(arr, sum, index+1, dp) or self.recursive(arr, sum-arr[index], index+1, dp)
        dp[index][sum] = ans
        return dp[index][sum]
        
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp = [[-1 for j in range(sum+1)] for i in range(N+1)]
        return self.recursive(arr, sum, 0, dp)
    
    def tabulationDPBottomUp(self, N, arr, sum):
        dp = [[False for j in range(sum+1)] for i in range(N+1)]
        # I need dp[0][sum], so I will go reverse and sum will from 0
        for i in range(N+1):
            dp[i][0] = True
        for j in range(1, sum+1):
            dp[0][j] = False
        for i in range(N-1, -1, -1):
            for j in range(1, sum+1):
                if arr[i] > j:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j-arr[i]] or dp[i+1][j]
        # print(dp)
        return dp[0][sum]