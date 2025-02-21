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
def sample_game(empty_board):
    return Game(800, 600, empty_board)

# UT_03
class TestUT03:
    # Step 1
    def test_new_game_object(self, sample_game):
        assert sample_game.width == 800
        assert sample_game.height == 600
        assert isinstance(sample_game.board, Board)
        assert len(sample_game.board.cards) == 0
        assert len(sample_game.board.flipped_cards) == 0
    # # Step 2
    def test_function_to_start_game(self, sample_game):
        sample_game.start_new_game()
        assert len(sample_game.board.cards) > 0
        assert len(sample_game.board.flipp_cards) == 0
        # Check if a card if not flipped or matched
        card = sample_game.cards[0]
        assert card.is_revealed == False
        assert card.is_matched == False
        



    # # Step 3
    # def test_board_is_initialised():