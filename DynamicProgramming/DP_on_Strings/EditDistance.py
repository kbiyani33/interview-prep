from sys import stdin
import sys
sys.setrecursionlimit(10**7)

def getEditDistance(str1, str2, i, j, dp):
    # If str2 is empty that means, I am supposed to delete remaining characters in str1
    if j==len(str2):
        return len(str1) - i
    if i == len(str1):
        return len(str2) - j
    if dp[i][j] != -1:
        return dp[i][j]
    if str1[i] == str2[j]:
        ans = getEditDistance(str1, str2, i+1, j+1, dp)
    else:
        insert = 1 + getEditDistance(str1, str2, i, j+1, dp) # I insert from str2[j] into str1 and keep i as it is and move j
        delete = 1 + getEditDistance(str1, str2, i+1, j, dp) # I delete from str1, so I still want to match str2[j]
        replace = 1 + getEditDistance(str1, str2, i+1, j+1, dp) # replaced in str1 to equal value and then moveing both
        ans = min(insert, delete, replace)

    dp[i][j] = ans
    return dp[i][j]

def editDistance(str1, str2) :
    m, n = len(str1), len(str2)
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    return getEditDistance(str1, str2, 0, 0, dp)

def tabulationDPBottomUp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if j==n:
                dp[i][j] = m-i
                continue
            if i==m:
                dp[i][j] = n-j
                continue

            if str1[i]==str2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                insert = 1 + dp[i][j+1]
                delete = 1 + dp[i+1][j]
                replace = 1 + dp[i+1][j+1]
                dp[i][j] = min(insert, delete, replace)
    return dp[0][0]

