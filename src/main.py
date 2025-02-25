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
        # Current game state
        self.game_state = "MENU"
        # Colour constans for screens
        self.PASTEL_PURPLE = (177, 156, 217)
        self.PURPLE = (128, 0, 128)
        self.PASTEL_GREEN = (119, 221, 119)
        self.PASTEL_RED = (255, 105, 97)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.PURPLE = (128, 0, 128)
        # Font constants for screens
        self.large_font = pygame.font.SysFont("Arial", 72)
        self.medium_font = pygame.font.SysFont("Arial", 36)
        # Menu buttons
        self.start_button = pygame.Rect(300, 200, 200, 50)
        self.exit_button = pygame.Rect(300, 300, 200, 50)
        # Win screen button
        self.continue_button = pygame.Rect(250, 350, 200, 50)
        # Current level
        self.current_level = 1
        # Initialising game
        self.board = Board(self.width, self.height)
        self.game = Game(self.width, self.height, self.board)

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


