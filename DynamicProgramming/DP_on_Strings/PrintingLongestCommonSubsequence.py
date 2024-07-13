"""
Given two sequences, print the longest subsequence present in both of them.
Example:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
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

if __name__ == "__main__":
    first = "abac"
    second = "cab"

    print(length_shortest_common_supersequence(first,second))
    print(printScs(first, second))


def tabulationDp_BottomUp(s, t):
    m, n = len(s), len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # I need to return dp[0][0] so i'll move backwards
    for i1 in range(m-1, -1, -1):
        for i2 in range(n-1, -1, -1):
            if s[i1]==t[i2]:
                dp[i1][i2] = 1 + dp[i1+1][i2+1]
            else:
                dp[i1][i2] = max(dp[i1][i2+1], dp[i1+1][i2])
    
    i, j, lcsStr = 0, 0, ""
    while i<m and j<n:
        if s[i]==t[j]:
            lcsStr += s[i]
            i += 1
            j += 1
            continue
        if dp[i+1][j] > dp[i][j+1]:
            i += 1
        else:
            j += 1
    print(lcsStr)
        
    return dp[0][0]

def lcs(s, t) :
    # m, n = len(s), len(t)
    # dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
    # return recursive_lcs(s, t, 0, 0, dp)
    return tabulationDp_BottomUp(s, t)