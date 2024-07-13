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
    
# CODE FOR CODE STUDIO

def countOfDistinctSubsequences(st:str, sub:str, index1:int, index2:int, dp) -> int:
    MOD = 1000000007
    if index2 == len(sub):
        return 1
    if index1 == len(st):
        return 0
    
    if dp[index1][index2] != -1:
        return dp[index1][index2]
    
    notTaken = countOfDistinctSubsequences(st, sub, index1+1, index2, dp)
    if st[index1] == sub[index2]:
        taken = countOfDistinctSubsequences(st, sub, index1+1, index2+1, dp)
        ans = (taken % MOD + notTaken % MOD) % MOD
    else:
        ans = notTaken
    dp[index1][index2] = ans
    return ans

def TabulationTopDown(st:str, sub:str) -> int:
    # write your code here
    
    MOD = 1000000007
    m, n = len(st), len(sub)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # BASE CASE CALCULATIONS
    # When len(sub) is reached, it's gonna be 1 for all cells until len of st Because of possibility of empty subsequence
    # When len(st) is reached for all cells except for 0 in j it'll be 0

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if j==n:
                dp[i][j] = 1
                continue
            if i==m:
                dp[i][j] = 0
                continue
            if st[i]==sub[j]:
                dp[i][j] = (dp[i+1][j+1] % MOD + dp[i+1][j] % MOD) % MOD
            else:
                dp[i][j] = dp[i+1][j]
    return dp[0][0]

def distinctSubsequences(str: str, sub: str) -> int:
    # write your code here
    
    dp = [[-1 for _ in range(len(sub)+1)] for _ in range(len(str)+1)]
    return countOfDistinctSubsequences(str, sub, 0, 0, dp)