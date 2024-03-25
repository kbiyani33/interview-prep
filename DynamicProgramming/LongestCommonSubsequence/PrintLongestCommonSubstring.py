"""
Given two strings X, Y, print the longest common substring. 

Examples : 

Input : X = "GeeksforGeeks", y = "GeeksQuizfor" 
Output : 5 
Explanation:
The longest common substring is "Geeks" and is of length 5.

Input : X = "abcdxyz", y = "xyzabcd" 
Output : 4 
Explanation:
The longest common substring is "abcd" and is of length 4.

Input : X = "zxabcdezy", y = "yzabcdezx" 
Output : 6 
Explanation:
The longest common substring is "abcdez" and is of length 6.
"""

from typing import List
import math

def getLCSDPMatrix(first:str, second:str) -> List[List[int]]:
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
                dp[i][j] = 0
    return dp

if __name__ == "__main__":
    first = "GeeksforGeeks"
    second = "GeeksforQuiz"
    dp_matrix_lcs = getLCSDPMatrix(first, second)
    I, J = 0, 0
    overallMax = -math.inf
    for i in range(len(first)+1):
        for j in range(len(second)+1):
            if dp_matrix_lcs[i][j] > overallMax:
                overallMax = dp_matrix_lcs[i][j]
                I = i
                J = j
    
    # If I find the value of I and J it means that the longest common substring is gonna be
    print(I, J)
    print(overallMax)

    op = ""
    for i in range(I-overallMax, I):
        op += first[i]
    print(op)
    op = ""
    for j in range(J-overallMax, J):
        op += second[j]
    print(op)


