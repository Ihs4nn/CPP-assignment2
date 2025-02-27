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
        # Buttons
        button_width = 200
        button_height = 50
        self.start_button = pygame.Rect((self.width - button_width) // 2, self.height // 2, button_width, button_height)
        self.exit_button = pygame.Rect((self.width - button_width) // 2, (self.height // 2) + 100, button_width, button_height)
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

    # AI Helped
    def draw_game(self):
        self.screen.fill(self.WHITE)
        # Draw level text
        level_text = self.medium_font.render("", True, self.BLACK)
        level_text_rect = level_text.get_rect(center=(self.width // 2, 30))
        self.screen.blit(level_text, level_text_rect)
        # Draw all cards
        for card in self.game.board.cards:
            # Draw card border
            border_rect = pygame.Rect(card.x - 2, card.y - 2, card.width + 4, card.height + 4)
            pygame.draw.rect(self.screen, self.BLACK, border_rect)
            # Draw card background
            card_rect = pygame.Rect(card.x, card.y, card.width, card.height)
            if card.is_revealed or card.is_matched:
                # Card is face up - pastel purple background
                pygame.draw.rect(self.screen, self.PASTEL_PURPLE, card_rect)
                # Display the acronym in black
                term_font = pygame.font.SysFont("Arial", 28)
                term_text = term_font.render(card.term, True, self.BLACK)
                term_rect = term_text.get_rect(center=(card.x + card.width // 2, card.y + card.height // 2))
                self.screen.blit(term_text, term_rect)
            else:
                # Card is face down - purple background with question mark
                pygame.draw.rect(self.screen, self.PURPLE, card_rect)
                question_font = pygame.font.SysFont("Arial", 36)
                question_text = question_font.render("?", True, self.WHITE)
                question_rect = question_text.get_rect(center=(card.x + card.width // 2, card.y + card.height // 2))
                self.screen.blit(question_text, question_rect)
        # Display definition at bottom of screen if there's a match
        if self.game.current_definition:
            definition_font = pygame.font.SysFont("Arial", 24)
            definition_text = definition_font.render(self.game.current_definition, True, self.BLACK)
            # Create a text box with fixed height
            def_box_width = min(800, self.width - 40)
            box_height = 60 
            # Create and draw text box
            def_box = pygame.Rect((self.width - def_box_width) // 2, self.height - box_height - 20, def_box_width, box_height)
            pygame.draw.rect(self.screen, self.PASTEL_PURPLE, def_box)
            pygame.draw.rect(self.screen, self.BLACK, def_box, 2)
            # Center the text in the box
            def_text_rect = definition_text.get_rect(center=(def_box.x + def_box_width // 2, def_box.y + box_height // 2))
            self.screen.blit(definition_text, def_text_rect)
        # End of AI help

    def draw_win(self):
        self.screen.fill(self.PASTEL_GREEN)
        game_text = self.large_font.render("Congratulations, you win!", True, self.WHITE)
        self.screen.blit(game_text, game_text.get_rect(center=(self.width // 2, self.height // 2)))
        # Draw the Exit button
        pygame.draw.rect(self.screen, self.PASTEL_RED, self.exit_button)
        exit_text = self.medium_font.render("Exit", True, self.BLACK)
        exit_text_rect = exit_text.get_rect(center=self.exit_button.center)
        self.screen.blit(exit_text, exit_text_rect)

    def handle_click(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Only check for button collisions on mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.game_state == "MENU":
                    # Checks if start button was clicked
                    if self.start_button.collidepoint(mouse_pos):
                        # Change game state and start a new game
                        self.game_state = "PLAY"
                        self.game.start_new_game()
                    # Checks if the exit button was clicked
                    elif self.exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                # AI Helped
                elif self.game_state == "PLAY":
                    # Check if any card was clicked
                    for card in self.game.board.cards:
                        card_rect = pygame.Rect(card.x, card.y, card.width, card.height)
                        if card_rect.collidepoint(mouse_pos) and not card.is_revealed and not card.is_matched:
                            self.game.handle_card_click(card)
                        # End of AI help
                # Check if the game has been completed
                elif self.game_state == "WIN":
                    if self.exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self.handle_click()
            # If the state is 'menu' draw the menu screen
            if self.game_state == "MENU":
                self.draw_menu()
            # If its 'play', draw the game screen
            elif self.game_state == "PLAY":
                get_state = self.game.update_flip()
                # Check for a win each time
                if get_state == "WIN":
                    self.game_state = "WIN"
                self.draw_game()
            # If its 'win', draw the win screen
            elif self.game_state == "WIN":
                self.draw_win()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game_screen = GameScreen(1000, 1000)
    game_screen.run()


