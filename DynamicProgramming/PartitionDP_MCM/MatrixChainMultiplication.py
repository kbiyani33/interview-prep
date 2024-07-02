"""
geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Given the dimension of a sequence of matrices in an array arr[], where the dimension of the ith matrix is (arr[i-1] * arr[i]), the task is to find the most efficient way to multiply these matrices together such that the total number of element multiplications is minimum.

Input: arr[] = {40, 20, 30, 10, 30}
Output: 26000
Explanation:There are 4 matrices of dimensions 40×20, 20×30, 30×10, 10×30.
Let the input 4 matrices be A, B, C and D.
The minimum number of  multiplications are obtained by 
putting parenthesis in following way (A(BC))D.
The minimum is 20*30*10 + 40*20*10 + 40*10*30

Input: arr[] = {1, 2, 3, 4, 3}
Output: 30
Explanation: There are 4 matrices of dimensions 1×2, 2×3, 3×4, 4×3. 
Let the input 4 matrices be A, B, C and D.  
The minimum number of multiplications are obtained by 
putting parenthesis in following way ((AB)C)D.
The minimum number is 1*2*3 + 1*3*4 + 1*4*3 = 30
"""

"""
For an array of size N, we can have upto N-1 matrices
The matrices are A1, A2, A3, ..., AN-1

Size(A1) = arr[0]*arr[1]
.
.
.
Size(Ak) = arr[k-1]*arr[k]
"""

"""
IDENTIFICATION that it's matrix chain multiplication

We have a range of i and j. And position of k is gonna make different possible positions of the brackets from starting
The function is gonna be minimum in this case.

Step1 --> is to see if the input is array or not. Is it ? Yes.
Step2 --> Chose values of i and j
        i can start from 0 ?
            No because we don't have circular dependencies and A0 cannot be formed.
        i can be 1 ?
            Yes, since the A1 can be arr[0]*arr[1]
        j can be right most value ?
            Yes Since AJ can be formed.
        i = 1 and j = N-1(N = length of the array)
Step3 --> Find base condition
        i > j is invalid since it means that the size of the array is 0
        Is i==j alright ? It means we have exactly one element in the array, that means 0 arrays. So even this is not possible.
        So the base condition can be if i >= j
"""

from os import *
from sys import *
from collections import *
from math import *
from typing import List

def bottomUp(arr:List[int], n:int):
	dp = [[0]*n for i in range(n)]
	for i in range(n-1, 0, -1):
		for j in range(i+1, n): # i+1 to n-1 because, j is always on the right(imagine 1,2,3,4 and I need to multiply everything from 1 to n-1, so j in partition is on the right)
			minI = inf
			for k in range(i, j):
				ans = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
				minI = min(minI, ans)
			dp[i][j] = minI
	return dp[1][n-1]

def recursiveMCM(arr:List[int], n:int, i:int, j:int, dp:List[List[int]]):
    # base case is when i and j are equal. Which means, there's just one single matrix in question
	if dp[i][j] != -1:
		return dp[i][j] 
	if i==j:
		dp[i][j] = 0
		return 0
	minI = inf
	for k in range(i, j):
		ans = recursiveMCM(arr, n, i, k, dp) + recursiveMCM(arr, n, k+1, j, dp) + arr[i-1]*arr[k]*arr[j]
		minI = min(minI, ans)
	dp[i][j] = minI
	return minI

def matrixMultiplication(arr:List[int], n:int):
	return bottomUp(arr, n)
	# dp = [[-1]*(n+1) for i in range(n+1)]
	# return recursiveMCM(arr, n, 1, n-1, dp)
	
