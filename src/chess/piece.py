"""
    chess.piece.py
    Authors: Vaxeral
    March 22 2021
    Chess version 0.1.0
    Descrition: Chess in pygame
"""

from typing import ClassVar
from typing import Tuple
from typing import Type
from typing import List
from chess.enums import File, Rank, Set

class ChessPiece:
    def __init__(self, cset: Set, board: 'ChessBoard', file: File, rank: Rank):
        self.cset: Set = cset
        self.board: 'ChessBoard' = board
        self.file: File = file
        self.rank: Rank = rank

    def __str__(self):
        return f"{self.cset} {self.__class__.name} at {self.file}{self.rank}"

    def is_valid_move(self, fm: Tuple[int, int], to: Tuple[int, int]) -> bool:
        return True

    def possible_moves(self):
        pass

    def update(self):
        pass

class King(ChessPiece):
    name: ClassVar[str] = "King"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)

class Queen(ChessPiece):
    name: ClassVar[str] = "Queen"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)

class Rook(ChessPiece):
    name: ClassVar[str] = "Rook"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)

class Bishop(ChessPiece):
    name: ClassVar[str] = "Bishop"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)

class Knight(ChessPiece):
    name: ClassVar[str] = "Knight"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)

class Pawn(ChessPiece):
    name: ClassVar[str] = "Pawn"
    def __init__(self, *args):
        ChessPiece.__init__(self, *args)
