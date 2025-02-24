import pytest
import pygame
import sys
from pygame import event
from pygame.rect import Rect
from src.main import GameScreen

@pytest.fixture
def start():
    pygame.init()
    start = GameScreen(800, 600)
    return start

class TestUT07:
    # Step 1
    def test_menu_initalisation(self, start):
        # Check if it has the correct title
        assert start.title == "Flip 'n' Find"
        # Check if the buttons have the correct dimensions
        assert start.start_button.x == 300
        assert start.start_button.y == 200
        assert start.exit_button.x == 300
        assert start.exit_button.y == 300
    # Step 2
    def test_user_click_start(self, start):
        # Check it is first in the main menu
        assert start.game_state == "MENU"
        # Handle user mouse click on 'Start'
        click_start = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (350, 225)})
        pygame.event.post(click_start)
        # Call function used to handle the clicks
        start.handle_click()
        # Checks if based on the click, the event state changes accordingly
        assert start.game_state == "PLAY"
        # Check if the game initalises
        assert len(start.game.board.cards) > 0
    # Step 3
    def test_user_click_exit(self, start, mocker):
        # Mocking functions used to quit and exit the application
        mocker.patch('pygame.quit')
        mocker.patch('sys.exit')
        assert start.game_state == "MENU"
        click_exit = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (350, 325)})
        pygame.event.post(click_exit)
        start.handle_click()
        # Check if the application does close
        pygame.quit.assert_called_once()
        sys.exit.assert_called_once()





        





