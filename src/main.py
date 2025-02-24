import pygame
import sys
from src.game import Game
from src.game import Board

class GameScreen:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        # Title of the game
        self.title = "Flip 'n' Find"
        pygame.display.set_caption(self.title)
        # Start and Exit buttons
        self.start_button = pygame.Rect(300, 200, 200, 50)
        self.exit_button = pygame.Rect(300, 300, 200, 50)
        self.board = Board(self.width, self.height)
        self.game = Game(self.width, self.height, self.board)
        self.game_state = "MENU"

    def handle_click(self):
        # Gets the events
        for event in pygame.event.get():
            # Only check for button collisions on mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Checks if start button was clicked
                if self.start_button.collidepoint(event.pos):
                    # Change game state and start a new game
                    self.game_state = "PLAY"
                    self.game.start_new_game()
                # Checks if the exit button was clicked
                elif self.exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


