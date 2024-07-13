from typing import *
finalAns = -1
def recursiveSolution(n:int, points:List[List[int]], day:int, previous:int, dp:List[int]) -> int:
    if day==n:
        return 0
    if dp[day][previous] != -1:
        return dp[day][previous]
    # basically get an answer by chosing a task that is not previous task and get the maximum
    maxI = -1
    for i in range(3):
        if i!= previous:
            ans = points[day][i]+recursiveSolution(n, points, day+1, i, dp)
            maxI = max(maxI, ans)
    dp[day][previous] = maxI
    return maxI

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    dp = [[-1]*4 for i in range(n)]
    return recursiveSolution(n, points, 0, 3, dp)
    
def tabulationBottomUp(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    # my final answer is dp[0][3] meaninng
    # Step 1 is copy the base case
    if n==0:
        return 0
    
    # Step 2 is identifying the changing variables and nesting them in reverse order of our final answer
    # my final answer is dp[0][3] meaninng i will move from n-1 to 0 and j will move from 0 to 3
    dp = [[0]*4 for i in range(n+1)]
    for day in range(n-1, -1, -1):
        for previous in range(4):
            # step 3 is copy the recurrence
            maxI = -1
            for i in range(3):
                if i!= previous:
                    ans = points[day][i] + dp[day+1][i]
                    maxI = max(ans, maxI)
            dp[day][previous] = maxI
    
    return dp[0][3]
