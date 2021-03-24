"""
    chess.board.py
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
from chess.piece import ChessPiece, Rook, Bishop, Knight, Queen, King, Pawn
from chess.player import Player

class Board:
    def __init__(self):
        self.board = []
        self.valid = []

    def standard_init(self):
        self.board = [ [None] * 8 for i in range(8) ]

        self.valid = [ [1] * 8 for i in range(8) ]

    def standard_fill(self):
        self.add_piece(Rook,   Set.WHITE, File.A, Rank.ONE)
        self.add_piece(Knight, Set.WHITE, File.B, Rank.ONE)
        self.add_piece(Bishop, Set.WHITE, File.C, Rank.ONE)
        self.add_piece(Queen,  Set.WHITE, File.D, Rank.ONE)
        self.add_piece(King,   Set.WHITE, File.E, Rank.ONE)
        self.add_piece(Bishop, Set.WHITE, File.F, Rank.ONE)
        self.add_piece(Knight, Set.WHITE, File.G, Rank.ONE)
        self.add_piece(Rook,   Set.WHITE, File.H, Rank.ONE)
        self.add_piece(Pawn,   Set.WHITE, File.A, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.B, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.C, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.D, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.E, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.F, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.G, Rank.TWO)
        self.add_piece(Pawn,   Set.WHITE, File.H, Rank.TWO)

        self.add_piece(Rook,   Set.BLACK, File.A, Rank.EIGHT)
        self.add_piece(Knight, Set.BLACK, File.B, Rank.EIGHT)
        self.add_piece(Bishop, Set.BLACK, File.C, Rank.EIGHT)
        self.add_piece(Queen,  Set.BLACK, File.D, Rank.EIGHT)
        self.add_piece(King,   Set.BLACK, File.E, Rank.EIGHT)
        self.add_piece(Bishop, Set.BLACK, File.F, Rank.EIGHT)
        self.add_piece(Knight, Set.BLACK, File.G, Rank.EIGHT)
        self.add_piece(Rook,   Set.BLACK, File.H, Rank.EIGHT)
        self.add_piece(Pawn,   Set.BLACK, File.A, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.B, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.C, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.D, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.E, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.F, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.G, Rank.SEVEN)
        self.add_piece(Pawn,   Set.BLACK, File.H, Rank.SEVEN)
        
    def is_valid_square(self, file: File, rank: Rank) -> bool:
        return self.valid[rank][file]

    def add_piece(self, cls: Type[ChessPiece], cset: Set, file: File, rank: Rank):
        if not self.is_valid_square(file, rank):
            raise ChessException(f"Tried to place a {cls.name} on an invalid square.")

        if self.get_piece(file, rank):
            raise ChessException(f"Tried to place a {cls.name} on an occupied square.")

        piece = cls(cset, self, file, rank)

        self.board[rank][file] = piece

    def get_piece(self, file: File, rank: Rank) -> ChessPiece:
        piece = self.board[rank][file]
        return piece

    def move_piece(self, player: Player, fm: Tuple[int, int], to: Tuple[int, int]):
        traveler = self.get_piece(fm[0], fm[1])
        if not traveler:
            raise ChessException("No piece found at {file}{rank}.")

        if not self.is_valid_square(to[0], to[1]):
            raise ChessException("Square {file}{rank} is invalid.")

        if not traveler.is_valid_move(fm[0], fm[1], to[0], to[1]):
            raise ChessException("traveler.__str__() cant move to square {file}{rank}")
