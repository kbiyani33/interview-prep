from model.PlayingPiece import PlayingPiece

class Player:
    def __init__(self, name:str, piece: PlayingPiece):
        self.name = name
        self.piece = piece
