from typing import List,Set,Tuple

class Solution:
    def findPath(self, matrix: List[List[int]]) -> List[str]:
        def backtracking(row:int, col:int, path:str, visited:Set[Tuple[int]]) -> None:
            if row==n-1 and col==n-1:
                result.append(path)
                return
            if not(0<=row<n) or not(0<=col<n) or matrix[row][col]==0 or (row,col) in visited:
                return
            # move left
            visited.add((row,col))
            backtracking(row,col-1,path+"L",visited)
            backtracking(row-1,col,path+"U",visited)
            backtracking(row,col+1,path+"R",visited)
            backtracking(row+1,col,path+"D",visited)
            visited.remove((row,col))
            return
        
        n = len(matrix)
        if n==0 or matrix[0][0]==0 or matrix[n-1][n-1]==0:
            return []
        result = []
        backtracking(0,0,"")
        return result