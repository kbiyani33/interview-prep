from typing import List
class Solution:
    def dfs(self, board: List[List[str]], word: str, row:int, col:int, visited:List[List[int]], index:int) -> bool:
        if index == len(word):
            return True
        m,n = len(board), len(board[0])
        if row<0 or row>=m or col<0 or col>=n or board[row][col] != word[index] or [row,col] in visited:
            return False
        # append the visited and go to any of the 4 directions which are not already visited
        visited.append([row,col])
        
        # call recursive calls on any one of the 4 places
        if (self.dfs(board, word, row,col-1, visited, index+1) or
            self.dfs(board, word, row-1,col, visited, index+1) or
            self.dfs(board, word, row,col+1, visited, index+1) or
            self.dfs(board, word, row+1,col, visited, index+1)):
            return True
        visited.pop()
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j, [], 0):
                        return True
        return False