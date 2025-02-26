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
            ("CRM", "Customer Relationship Management - Client interaction system"),
            ("SEO", "Search Engine Optimization - Improving website visibility"),
            ("CMS", "Content Management System - Website content handling")
        ]
        self.current_definition = ""
        # Used to handle time delay
        self.waiting = False
        self.wait_start_time = 0
        self.wait_delay = 1000
        # Variable to store waiting definition
        self.pending_definition = None

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
                self.pending_definition = self.board.flipped_cards[0].definition
                pygame.display.flip()
                self.waiting = True
                self.wait_start_time = pygame.time.get_ticks()
    
    # Function used to wait for the second card to flip
    def update_flip(self):
        if self.waiting:
            current_time = pygame.time.get_ticks()
            # Checks if enough time has passed for the user to look at the second card
            if current_time - self.wait_start_time >= self.wait_delay:
                # If enough time has passed, then check if they match
                found_pair = self.board.check_match()
                if found_pair:
                    # Stores the pending definition in the current one as they do match
                    self.current_definition = self.pending_definition
                    # Checks for a win if a found pair has been matched
                    if self.check_win():
                        return "WIN"
                else:
                    self.current_definition = None
                self.pending_definition = None
                self.waiting = False
        return "PLAY"

    # Function to check if all cards are matched for a win
    def check_win(self):
        return all(card.is_matched for card in self.board.cards)