from model.PlayingPiece import PlayingPiece
from model.PieceType import PieceType

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(pieceType=PieceType.O)