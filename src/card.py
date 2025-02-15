import pygame
from typing import Tuple

class Card:
    def __init__(self, value, x, y, width, height, definition):
        self.value = value
        self.definition = definition
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Cards should be face down at the start
        self.is_revealed = False
        self.is_matched = False

    # Function to flip the card
    def flip_card(self):
        self.is_revealed = True
    
    # Function to mark the card as matched