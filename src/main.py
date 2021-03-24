"""
    main.py
    Authors: Vaxeral
    March 22 2021
    Chess version 0.1.0
    Descrition: Chess in pygame

    TODO: Learn the basics of pygame.  Drawing, Input Handling, ...
"""

from chess.player import Player as ChessPlayer
from chess.board import Board as ChessBoard

p = ChessPlayer()
b = ChessBoard()
b.standard_init()
b.standard_fill()
