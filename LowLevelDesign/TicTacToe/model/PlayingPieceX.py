from model.PlayingPiece import PlayingPiece
from model.PieceType import PieceType

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(pieceType=PieceType.X)