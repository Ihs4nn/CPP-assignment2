import pygame
from typing import List, Tuple
from .board import Board

class Game:
    def __init__(self, width: int, height: int, board: Board):
        self.width = width
        self.height = height
        self.board = board
        self.flipped_cards = []
