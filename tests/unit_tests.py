import pytest
from src.board import Board
from src.card import Card

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
def sample_board(sample_terms):
    board = Board(800, 600)
    board.create_grid(terms=sample_terms, cols=4, rows=4)
    return board


# UT_01
class test_UT_01:
    # Step 1
    def test_board_dimensions(self, sample_board):
        assert sample_board.width == 800
        assert sample_board.height == 600

    def test_number_of_cards(self, sample_board):
        assert len(sample_board.cards) == 16
    
    # Step 2
    

