from typing import Optional, Deque
from collections import deque

from model.Board import Board
from model.Player import Player
from model.PlayingPieceX import PlayingPieceX
from model.PlayingPieceO import PlayingPieceO

class TicTacToeGame:
    def __init__(self):
        self.players: Deque[Player] = deque()

    def initializeGame(self):
        self.gameBoard = Board(size=3)
        crossPiece = PlayingPieceX()
        oPiece = PlayingPieceO()

        self.players.append(Player(name="Player1", piece=crossPiece))
        self.players.append(Player(name="Player2", piece=oPiece))

    def startGame(self) -> str:
        gameBoard, players = self.gameBoard, self.players

        while True:
            if not gameBoard.getFreeCells():
                return "tie"

            currentPlayer = players.popleft()

            print(f"It's {currentPlayer.name}'s turn.")
            try:
                row, col = map(int, input("Enter row,col (e.g., 0,0): ").split(","))
            except ValueError:
                print("Invalid input format. Try again.")
                players.appendleft(currentPlayer)
                continue

            pieceAdded = gameBoard.addPiece(row, col, currentPlayer.piece)
            if not pieceAdded:
                print("Invalid position. Try again.")
                players.appendleft(currentPlayer)
                continue

            gameBoard.printBoard()
            if self.isThereAWinner(row, col, currentPlayer):
                return f"{currentPlayer.name} wins!"

            players.append(currentPlayer)

    def isThereAWinner(self, row: int, col: int, player: Player) -> bool:
        gameBoard = self.gameBoard.boardPieces
        pieceType = player.piece.pieceType.value  # "X" or "O"
        size = self.gameBoard.size

        # Check row
        if all(gameBoard[row][j] and gameBoard[row][j].pieceType.value == pieceType for j in range(size)):
            return True

        # Check column
        if all(gameBoard[i][col] and gameBoard[i][col].pieceType.value == pieceType for i in range(size)):
            return True

        # Check main diagonal
        if row == col and all(gameBoard[i][i] and gameBoard[i][i].pieceType.value == pieceType for i in range(size)):
            return True

        # Check anti-diagonal
        if row + col == size - 1 and all(gameBoard[i][size - 1 - i] and gameBoard[i][size - 1 - i].pieceType.value == pieceType for i in range(size)):
            return True

        return False
