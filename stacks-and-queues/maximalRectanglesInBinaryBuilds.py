from typing import List

class Solution:
    def maximumAreaHistogram(self, row:List[int]) -> int:
        print(row)
        maxArea = 0
        n = len(row)
        stack = []
        for i in range(n):
            while stack and row[stack[-1]] > row[i]:
                element = stack.pop()
                pse = stack[-1] if stack else -1
                maxArea = max(maxArea, (i-pse-1)*row[element])
            stack.append(i)
        while stack:
            element = stack.pop()
            nse = n
            pse = stack[-1] if stack else -1
            maxArea = max(maxArea, (nse-pse-1)*row[element])
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        topDown = [[0]*n for i in range(m)]
        topDown[0] = [int(i) for i in matrix[0]]
        maxI = self.maximumAreaHistogram(topDown[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]=="0":
                    topDown[i][j] = 0
                else:
                    topDown[i][j] = topDown[i-1][j]+1
            maxI = max(maxI, self.maximumAreaHistogram(topDown[i]))
        return maxI