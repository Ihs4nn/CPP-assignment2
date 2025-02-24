import pytest
import pygame
from src.main import StartMenu

@pytest.fixture
def menu():
    pygame.init()
    menu = StartMenu(width=800, height=600)
    return menu

class TestUT07:
    # Step 1
    def test_menu_initalisation(self, menu):
        assert menu.title == "Flip 'n' Find"
        assert menu.start_button.x == 300
        assert menu.start_button.y == 200
        assert menu.exit_button.x == 300
        assert menu.exit_button.y == 300