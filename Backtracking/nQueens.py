from typing import List
from copy import deepcopy

class Solution:

    """
    This function can be optimised using hashing. 
    1. For left upward diagonal, the value of (n-1 + col-row is constant)
    2. For left row, the value of row is constant
    3. For left downward diagonal, the value of row+col is constant
    """    
    def isValid(self, board:List[List[str]], row:int, col:int) -> bool:
        # Since i am filling from left to right, we don't case about the 3 directions on right(right, right downward diagonal, right upward digonal)
        # We also don't care about the upward and downward direction since no point place there
        # We search is 3 directions
        
        # 1. left upward diagonal
        cr, cc = row-1, col-1
        while(cr>=0 and cc>=0):
            if board[cr][cc] == "Q": return False
            cr -= 1
            cc -= 1
        
        # 2. left direction
        cr, cc = row, col
        while(cc >= 0):
            if board[cr][cc] == "Q": return False
            cc -= 1
        
        # 3. left downward diagonal
        cr, cc = row, col
        while(cr < len(board) and cc >= 0):
            if board[cr][cc] == "Q": return False
            cr += 1
            cc -= 1
        
        return True

    def placeQueens(self, col:int, board: List[List[str]], ans: List[List[str]], leftSameRow:List[bool], leftDownwardDiagonal:List[bool], leftUpwardDiagonal:List[bool]):
        # What are we trying to do here ?
        # I want to try and place a queen at the current column. And see if such a configuration is possible.
        # This is where the recursion takes place

        # base case is when I go out of the board.
        if col == len(board):
            ans.append(board.copy())
            return
        
        def isOptimisedValid(row, col):
            return (not leftSameRow[row]) and (not leftDownwardDiagonal[len(board)-1+col-row]) and (not leftUpwardDiagonal[row+col])
        # In the current col, I can place in n possible positions. So we will try and place in all 4 positions and see if its possible.
        for row in range(len(board)):
            # Check if row, col is a valid position. If yes, then place and continue
            if isOptimisedValid(row, col):
                # Set board and make the hashes
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                leftSameRow[row] = True
                leftDownwardDiagonal[len(board)-1+col-row] =  True
                leftUpwardDiagonal[row+col] = True

                # Call on new col
                self.placeQueens(col+1, board, ans, leftSameRow, leftDownwardDiagonal, leftUpwardDiagonal)

                # Now after it comes back here, remove the Q from row, col and continue and unmark hashes
                board[row] = board[row][:col] + "." + board[row][col+1:]
                leftSameRow[row] = False
                leftDownwardDiagonal[len(board)-1+col-row] =  False
                leftUpwardDiagonal[row+col] = False


    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<=3: return []

        ans = []
        # Initially the board is all blanks in n*n
        board = ["." * n for _ in range(n)]
        maxHashKeys = 2*n - 1
        """
            The isValid function can be optimised using hashing. 
            1. For left upward diagonal, the value of (n-1 + col-row is constant)
            2. For left row, the value of row is constant
            3. For left downward diagonal, the value of row+col is constant
        """ 
        leftSameRowHash = [False for _ in range(n)]
        leftUpwardDiagonal = [False for _ in range(maxHashKeys)]
        leftDownwardDiagonal = [False for _ in range(maxHashKeys)]
 
        self.placeQueens(0, board, ans, leftSameRowHash, leftDownwardDiagonal, leftUpwardDiagonal)
        return ans
    
if __name__=="__main__":
    soln = Solution()
    print(soln.solveNQueens(4))