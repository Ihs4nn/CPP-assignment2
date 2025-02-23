import pygame
from src.board import Board
from src.card import Card

class Game:
    def __init__(self, width: int, height: int, board: Board):
        self.width = width
        self.height = height
        self.board = board
        self.terms = [
            ("HR", "Human Resources - Department managing employee relations"),
            ("IT", "Information Technology - Technical support and infrastructure"),
            ("CEO", "Chief Executive Officer - Highest-ranking executive"),
            ("KPI", "Key Performance Indicator - Success metrics measurement"),
            ("ROI", "Return on Investment - Profitability measurement"),
            ("CRM", "Customer Relationship Management - Client interaction system")
        ]
        self.current_definition = ""

    # Function to initalise a new game
    def start_new_game(self):
        if not self.board.cards:
            self.board.create_grid(self.terms)
        self.board.flipped_cards = []
    
    # Function to handle when a user clicks a card
    def handle_card_click(self, card: Card):
        # If the flipped cards list is less then 2, flip a card
        if len(self.board.flipped_cards) < 2:
            card.flip_card()
            self.board.flipped_cards.append(card)
            # If the length is 2, check if they match
            if len(self.board.flipped_cards) == 2:
                found_pair = self.board.check_match()
                if found_pair:
                    self.current_definition = card.definition
                else:
                    self.current_definition = None

    # Function to check if all cards are matched for a win
    def check_win(self):
        return all(card.is_matched for card in self.board.cards)