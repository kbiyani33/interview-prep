class Solution:
    def topDownDP(self, s:str):
        s2 = "geek"
        m, n = len(s), 4
        mod = self.MODULO
        # Step 1 is to copy the base case
        dp = [[0]*(5) for i in range(m+1)]
        dp[0][0] = 1
        for i in range(m+1):
            dp[i][0] = 1
        
        # Step 2 is to nest the iteration of the 2 variables that are changing in the reverse direction of the answer needed.
        # We need dp[m][n] so I will go from 0 to m and 0 to n
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j] = (dp[i-1][j-1]%mod + dp[i-1][j]%mod)%mod
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]
    
    def geekCount(self, s : str) -> int:
        self.MODULO = 1000000007
        return self.topDownDP(s)
    
    def geekCountBottomUp(self, s : str) -> int:
        def count(a, b, m, n, dp): 
            # If both first and second string 
            # is empty, or if second string 
            # is empty, return 1 
            if ((m == 0 and n == 0) or n == 0): 
                return 1
         
            # If only first string is empty 
            # and second string is not empty,
            # return 0 
            if (m == 0):
                return 0
            
            if dp[m][n] != -1:
                return dp[m][n]
         
            # If last characters are same 
            # Recur for remaining strings by 
            # 1. considering last characters 
            #    of both strings 
            # 2. ignoring last character 
            #    of first string 
            if (a[m - 1] == b[n - 1]): 
                dp[m][n] = (count(a, b, m - 1, n - 1, dp) +
                        count(a, b, m - 1, n, dp)) 
            else:
                 
                # If last characters are different, 
                # ignore last char of first string 
                # and recur for remaining string 
                dp[m][n] = count(a, b, m - 1, n, dp)
            
            return dp[m][n]
        # code here
        # changable parameter = m and n
        dp = [[-1]*5 for i in range(len(s)+1)]
        return count(s, "geek", len(s), 4, dp)