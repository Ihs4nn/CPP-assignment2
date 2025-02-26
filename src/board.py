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

    # AI Helped
    def create_grid(self, terms, cols=4, rows=4):
        card_data = terms * 2 
        random.shuffle(card_data)

        card_width = 120
        card_height = 160
        spacing = 20

        total_width = cols * card_width + (cols - 1) * spacing
        total_height = rows * card_height + (rows - 1) * spacing
        start_x = (self.width - total_width) // 2
        start_y = (self.height - total_height) // 2

        # Create a list of cards
        self.cards = []
        for i, (acronym, definition) in enumerate(card_data):
            col = i % cols
            row = i // cols
            x = start_x + col * (card_width + spacing)
            # End of AI help
            y = start_y + row * (card_height + spacing)
            card = Card(
                term = acronym, 
                definition = definition,
                x = x,
                y = y, 
                width = card_width, 
                height = card_height
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
                    card.reset_card()
            # Clear the list for the next round
            self.flipped_cards = []
            return is_match
        return False

