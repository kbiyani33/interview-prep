from model.PlayingPiece import PlayingPiece
from typing import List, Optional

class Board:
    def __init__(self, size: int):
        self.size = size
        self.boardPieces: List[List[Optional[PlayingPiece]]] = [[None for _ in range(size)] for _ in range(size)]
    
    def addPiece(self, row: int, col: int, piece: PlayingPiece) -> bool:
        size, boardPieces = self.size, self.boardPieces

        if not (0 <= row < size and 0 <= col < size) or boardPieces[row][col]:
            return False
        
        boardPieces[row][col] = piece
        return True
    
    def getFreeCells(self) -> List[List[int]]:
        freeCells = [[i, j] for i in range(self.size) for j in range(self.size) if self.boardPieces[i][j] is None]
        return freeCells

    def printBoard(self) -> None:
        for row in self.boardPieces:
            print("|".join(piece.pieceType.value if piece else " " for piece in row))
            print("-" * (2 * self.size - 1))  # Row separator