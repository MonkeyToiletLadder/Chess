"""
    chess.enums.py
    Authors: Vaxeral
    March 22 2021
    Chess version 0.1.0
    Descrition: Chess in pygame
"""

from enum import IntEnum

class File(IntEnum):
    A = 0; B = 1; C = 2;
    D = 3; E = 4; F = 5;
    G = 6; H = 7

    def __str__(self):
        return self.name.lower()

class Rank(IntEnum):
    ONE   = 0; TWO   = 1; THREE = 2;
    FOUR  = 3; FIVE  = 4; SIX   = 5;
    SEVEN = 6; EIGHT = 7;

    def __str__(self):
        return str(self.value + 1)

class Set(IntEnum):
    BLACK = 0; WHITE = 1; RED = 2; BLUE = 3

    def __str__(self):
        return self.name.lower().capitalize()
