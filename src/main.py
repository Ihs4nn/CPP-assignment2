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
        button_width = 200
        button_height = 50
        self.start_button = pygame.Rect((self.width - button_width) // 2, self.height // 2, button_width, button_height)
        self.exit_button = pygame.Rect((self.width - button_width) // 2, (self.height // 2) + 100, button_width, button_height)
        # Win screen button
        self.continue_button = pygame.Rect((self.width - button_width) // 2, self.height // 2, button_width, button_height)
        # Current level
        self.current_level = 1
        # Initialising game
        self.board = Board(self.width, self.height)
        self.game = Game(self.width, self.height, self.board)

    def draw_menu(self):
        # Fill background with pastel purple
        self.screen.fill(self.PASTEL_PURPLE)
        # Draw Title
        title_text = self.large_font.render("Flip 'n' Find", True, self.WHITE)
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
        self.screen.blit(title_text, title_rect)
        # Draw the Start button
        pygame.draw.rect(self.screen, self.PASTEL_GREEN, self.start_button)
        start_text = self.medium_font.render("Start", True, self.BLACK)
        start_text_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_text_rect)
        # Draw the Exit button
        pygame.draw.rect(self.screen, self.PASTEL_RED, self.exit_button)
        exit_text = self.medium_font.render("Exit", True, self.BLACK)
        exit_text_rect = exit_text.get_rect(center=self.exit_button.center)
        self.screen.blit(exit_text, exit_text_rect)
    
    def draw_game(self):
        self.screen.fill(self.WHITE)
        game_text = self.medium_font.render("Hi, this is a temp page!", True, self.BLACK)
        self.screen.blit(game_text, game_text.get_rect(center=(self.width // 2, self.height // 2)))
    

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
    
    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.handle_click()
            if self.game_state == "MENU":
                self.draw_menu()
            elif self.game_state == "PLAY":
                self.draw_game()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game_screen = GameScreen(1000, 1000)
    game_screen.run()


