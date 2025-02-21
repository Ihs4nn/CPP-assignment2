import pygame
from src.board import Board

class Game:
    def __init__(self, width: int, height: int, board: Board):
        self.width = width
        self.height = height
        self.board = board
        self.flipped_cards = []
        self.terms = [
            ("HR", "Human Resources - Department managing employee relations"),
            ("IT", "Information Technology - Technical support and infrastructure"),
            ("CEO", "Chief Executive Officer - Highest-ranking executive"),
            ("KPI", "Key Performance Indicator - Success metrics measurement"),
            ("ROI", "Return on Investment - Profitability measurement"),
            ("CRM", "Customer Relationship Management - Client interaction system")
        ]

    def start_new_game(self):
        self.board.create_grid(self.terms)
        self.flipped_cards = []
