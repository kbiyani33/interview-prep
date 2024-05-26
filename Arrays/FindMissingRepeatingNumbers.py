from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        squareVal = N*N
        targetSum = (squareVal+1)*(squareVal//2) if N%2==0 else (squareVal+1)//2*(squareVal)
        targetSumSquares = (squareVal * (squareVal+1) * (2*(squareVal)+1)) // 6
        
        # Initialize variables to hold the actual sums of the grid elements and their squares
        actualSum = 0
        actualSumSquares = 0
        
        # Iterate through the grid to compute the actual sums
        for i in range(N):
            for j in range(N):
                actualSum += grid[i][j]
                actualSumSquares += grid[i][j] ** 2
        
        # Use the difference between the target and actual sums to find the missing and repeating numbers
        sumDiff = targetSum - actualSum
        sumSquaresDiff = targetSumSquares - actualSumSquares
        
        # Now, let's denote the missing number as x and the repeating number as y
        # We have the following two equations:
        # x - y = sumDiff
        # x^2 - y^2 = sumSquaresDiff
        # which simplifies to:
        # (x + y) = sumSquaresDiff / sumDiff
        
        # Solve for x and y
        x_plus_y = sumSquaresDiff // sumDiff
        x_minus_y = sumDiff
        
        # Now we have a system of two equations:
        # x + y = x_plus_y
        # x - y = x_minus_y
        # Adding them gives us 2x = x_plus_y + x_minus_y
        # So, we can find x:
        repeating = (x_plus_y - x_minus_y) // 2
        missing = repeating + x_minus_y
        
        return [repeating, missing]