"""
The idea in getting length is simple

The idea in getting the string is as follows

We traverse the LCS DP Matrix in the same way. however, we simply used to move in the direction of max(dp[i-1][j], dp[i][j-1]) earlier.
For supersequence, we will include that character as well.

And we will run loop again until both i and j become 0
"""
from typing import List

def getlcs(first:str, second:str) -> List[List[int]]:

    m = len(first)
    n = len(second)

    dp = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            elif first[i-1] == second[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def length_shortest_common_supersequence(first:str, second:str):
    dp_lcs = getlcs(first, second)
    return len(first) + len(second) - dp_lcs[-1][-1]

def printScs(str1:str, str2:str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[None]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        i = m
        j = n
        scs = ""
        while(i != 0 and j != 0):
            if str1[i-1] == str2[j-1]:
                # lcs_str = str1[i-1] + lcs_str
                scs = str1[i-1] + scs
                i -= 1
                j -= 1

            elif dp[i-1][j] > dp[i][j-1]:
                scs = str1[i-1] + scs
                i -= 1

            else:
                scs = str2[j-1] + scs
                j -= 1
        
        while(i > 0):
            scs = str1[i-1] + scs
            i -= 1
        
        while(j > 0):
            scs = str2[j-1] + scs
            j -= 1
            
        return scs