"""
Given two strings X, Y, find the length of the longest common substring. 

Examples : 

Input : X = “GeeksforGeeks”, y = “GeeksQuizfor” 
Output : 5 
Explanation:
The longest common substring is “Geeks” and is of length 5.

Input : X = “abcdxyz”, y = “xyzabcd” 
Output : 4 
Explanation:
The longest common substring is “abcd” and is of length 4.

Input : X = “zxabcdezy”, y = “yzabcdezx” 
Output : 6 
Explanation:
The longest common substring is “abcdez” and is of length 6.
"""

import time
import math

def lcs_dp(first:str, second:str) -> int:
    m = len(first)
    n = len(second)

    dp = [[None] * (n+1) for i in range(m+1)]
    """
    What is dp[m][n] referring to exactly ??
    It means that what's the answer of LCS output string length when we take only 
    first m and 
    first n 
    letters from first and second input string respectively.
    so dp[0][0] is LCS int with 0 letters in both first and last
    """
    maxVal = -math.inf
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif first[i-1] == second[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 0
    maxVal = -math.inf
    for i in range(m+1):
        for j in range(n+1):
            maxVal = max(maxVal, dp[i][j])
    return maxVal

overallMax = -math.inf
def recursiveLCS(first:str, second:str) -> int:
    if len(first) == 0 or len(second) == 0:
        return 0
    
    if first[0] == second[0]:
        maximum = 1 + recursiveLCS(first[1:], second[1:])


if __name__ == "__main__":
    first = "“zxabcdezy”"
    second = "“yzabcdezx”"
    # print(recursiveLCS(first, second))
    # start1 = time.time()
    # print(recursiveLCS(first, seco nd))
    # end1 = time.time()

    # print("recursive time is " + str(end1-start1))

    start2 = time.time()
    op = lcs_dp(first, second)
    print(op)
    end2 = time.time()
    print("DP time is " + str(end2-start2))




# CODE STUDIO CODE
def lcs(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # I need to return dp[0][0] so i'll move backwards
    ans = -1
    for i1 in range(m-1, -1, -1):
        for i2 in range(n-1, -1, -1):
            if s[i1]==t[i2]:
                dp[i1][i2] = 1 + dp[i1+1][i2+1]
                ans = max(ans, dp[i1][i2])
            else:
                dp[i1][i2] = 0
    return ans