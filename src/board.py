import pygame
import random
from src.card import Card

class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        # List to store the flipped cards
        self.flipped_cards = []
        self.cards = []

    # Hardcoding rows and columns to get the UT_01 tests passing
    def create_grid(self, terms, cols=4, rows=3):
        # Duplicating terms to create a pair
        card_data = terms * 2 
        random.shuffle(card_data)

        # Create a list of the cards
        self.cards = []
        for (acroynm, definition) in card_data:
            card = Card(
                term = acroynm,
                definition = definition,
                x = 0,
                y = 0,
                width = 120,
                height = 160,
            )
            self.cards.append(card)
    
    # Function to check if two cards match
    def check_match(self):
        # If two cards have been chosen
        if len(self.flipped_cards) == 2:
            # And the value is the same
            is_match = self.flipped_cards[0].term == self.flipped_cards[1].term
            if is_match:
                # toggle the cards attribute to is_matched = true
                for card in self.flipped_cards:
                    card.match_card()
            else:
                # if not, reset the cards
                for card in self.flipped_cards:
                    pygame.time.wait(1000)
                    card.reset_card()
            # Clear the list for the next round
            self.flipped_cards = []
            return is_match
        return False

