from os import *
from sys import *
from collections import *
from math import *
from typing import List


def maxValueInKnapsack(weights:List[int], values:List[int], capacity:int) -> int:
    n = len(weights)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # if my capacity is 0, then I can never take a value, so dp ans is 0
    # if my array elements are 0 even then I cannot take anything because obvious no elements, so no value :)

    for i in range(n-1, -1, -1):
        for j in range(1, capacity+1):
            if weights[i] > j:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(values[i] + dp[i+1][j-weights[i]], dp[i+1][j])
    
    return dp[0][capacity]


if __name__=="__main__":
    t = int(input())
    while(t>0):
        weights, values, capacity = [], [], []
        weights = [int(i) for i in input().strip().split(" ")]
        values = [int(i) for i in input().strip().split(" ")]
        capacity = int(input())

        print(maxValueInKnapsack(weights, values, capacity))
        t -= 1

from typing import List
class Solution:

    def tabulationBottomUp(self, capacity:int, weights:List[int], values:List[int], n:int):
        dp = [[0]*(capacity+1) for i in range(n+1)]
        # dp[i][j] is telling me what is the largest value i can obtain when filling a knapsack with weights until i'th index of array and sack having capacity of j
        for i in range(n+1):
            for j in range(capacity+1):
                if i==0 or j==0:
                    # meaning either 0 elements of 0 capacity, the answer is 0
                    dp[i][j] = 0
                elif weights[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
        return dp[n][capacity]
    
    def recursive(self, capacity:int, weights:List[int], values:List[int], index:int, dp:List[List[int]]) -> int:
        if dp[index][capacity] != -1:
            return dp[index][capacity]
        
        if index==len(weights):
            return 0
        if capacity==0:
            return 0
        ans = -1
        if weights[index] > capacity:
            ans = self.recursive(capacity, weights, values, index+1, dp)
        else:
            ans = max(self.recursive(capacity, weights, values, index+1, dp), values[index] + self.recursive(capacity-weights[index], weights, values, index+1, dp))
        dp[index][capacity] = ans
        return ans
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W:int, wt:List[int], val:List[int], n:int):
        # code here
        # W = capacity. If it's 0 then I cannot get anything right
        # dp = [[-1]*(W+1) for i in range(n+1)]
        return self.tabulationBottomUp(W, wt, val, n)