from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        spiral = []

        minRow, minCol = 0, 0
        maxRow, maxCol = m - 1, n - 1

        while minRow <= maxRow and minCol <= maxCol:
            # Firt moving right from minCol to 1 before maxCol
            for col in range(minCol, maxCol + 1):
                spiral.append(matrix[minRow][col])
            minRow += 1

            # Now from minRow to maxRow, we will go down and append the elements in maxCol
            for row in range(minRow, maxRow + 1):
                spiral.append(matrix[row][maxCol])
            maxCol -= 1

            # Now we will move left from maxCol to minCol+1(decrement) and append elements from last row
            if minRow <= maxRow:
                for col in range(maxCol, minCol - 1, -1):
                    spiral.append(matrix[maxRow][col])
                maxRow -= 1

            # Now move up from maxRow to 1 before minRow and get the elements from minCol
            if minCol <= maxCol:
                for row in range(maxRow, minRow - 1, -1):
                    spiral.append(matrix[row][minCol])
                minCol += 1

        return spiral
