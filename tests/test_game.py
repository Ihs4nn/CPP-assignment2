import pytest
from src.board import Board
from src.card import Card
from src.game import Game

# Creating fixtures
@pytest.fixture
def sample_terms():
    return [
    ("ADO", "Azure DevOps - software suite for tracking/deploying"),
    ("PAC", "Pre-Approved Change - for network switching"),
    ("EBU", "Enterprise Business Unit - business part of Vodafone"),
    ("FT",  "Fault Tolerance - system continues operating if errors occur"),
    ("MVA", "My Vodafone App - the customer app"),
    ("TLD", "Top Level Domain - e.g., .com, .org, .uk"),
    ("SSH", "Secure Shell - protocol for secure network communication"),
    ("CTN", "Customer Telephone Number - the user's phone number"),
]

@pytest.fixture
def empty_board():
    return Board(800, 600)

@pytest.fixture
def empty_game(empty_board):
    return Game(800, 600, empty_board)

@pytest.fixture
def start_game():
    board = Board(800, 600)
    new_game = Game(800, 600, board)
    return new_game

# UT_03
class TestUT03:
    # Step 1
    def test_new_game_object(self, empty_game):
        assert empty_game.width == 800
        assert empty_game.height == 600
        assert isinstance(empty_game.board, Board)
        assert len(empty_game.board.cards) == 0
        assert len(empty_game.board.flipped_cards) == 0
    # # Step 2
    def test_function_to_start_game(self, start_game):
        start_game.start_new_game()
        assert len(start_game.board.cards) > 0
        assert len(start_game.board.flipped_cards) == 0
        # Check if a card is not flipped or matched
        card = start_game.board.cards[0]
        assert card.is_revealed == False
        assert card.is_matched == False
    # # Step 3
    # def test_board_is_initialised():