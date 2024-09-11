from typing import List

class Solution:
    def maximumAreaHistogram(self, row:List[int]) -> int:
        maxI = 0
        stack = []
        n = len(row)
        for i in range(n+1):
            while stack and (i==n or row[stack[-1]]>=row[i]):
                top = stack.pop()
                height = row[top]
                width = 0
                if stack:
                    width = i-stack[-1]-1
                else:
                    width = i
                maxI = max(maxI, height*width)
            stack.append(i)
        return maxI

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