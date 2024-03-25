"""
given 2 string, return length of longest common subsequence

first   = abcdgh
second  = abedfh

LCS = abdh thus we return 4

What's the base condition
if even one of the strings has a length 0 then it's no point, return 0
"""

import time

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
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif first[i-1] == second[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


def recursiveLCS(first:str, second:str) -> int:

    if len(first) == 0 or len(second) == 0:
        return 0
    
    lastchar1 = first[-1]
    lastchar2 = second[-1]

    if lastchar1 == lastchar2:
        return 1+recursiveLCS(first[:-1], second[:-1])
    else:
        return max(recursiveLCS(first, second[:-1]), recursiveLCS(first[:-1], second))


if __name__ == "__main__":
    first = "abcdgf"
    second = "abdeghr"
    # print(recursiveLCS(first, second))
    start1 = time.time()
    print(recursiveLCS(first, second))
    end1 = time.time()

    print("recursive time is " + str(end1-start1))

    start2 = time.time()
    op = lcs_dp(first, second)
    print(op)
    end2 = time.time()
    print("DP time is " + str(end2-start2))

