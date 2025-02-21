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
# Matching terms
def matching_pair_terms():
    return [
        ("ADO", "Azure DevOps - software suite for tracking/deploying")
    ]

@pytest.fixture
def sample_board(sample_terms):
    board = Board(800, 600)
    board.create_grid(terms=sample_terms, cols=4, rows=3)
    return board

@pytest.fixture
def matching_sample_board(matching_pair_terms):
    matching_board = Board(800, 600)
    matching_board.create_grid(terms=matching_pair_terms, cols=4, rows=3)
    return matching_board

# UT_02
class TestUT02:
    # Step 1 
    def test_card_flipping(self, sample_board):
        # Get first two cards
        first_card = sample_board.cards[0]
        second_card = sample_board.cards[1]
        # Check to see if they are hidden at first
        assert first_card.is_revealed == False
        assert second_card.is_revealed == False
        # Flip the cards
        first_card.flip_card()
        second_card.flip_card()
        # Check to see if they are revealed
        assert first_card.is_revealed == True
        assert second_card.is_revealed == True

    # Step 2
    def test_card_matching_valid(self, matching_sample_board):
        # Get first two cards
        first_card = matching_sample_board.cards[0]
        second_card = matching_sample_board.cards[1]
        # Flip the cards
        first_card.flip_card()
        second_card.flip_card()
        # Add them to a list to check for a pair
        matching_sample_board.flipped_cards = [first_card, second_card]
        # Check if they match
        matching_sample_board.check_match()
        assert first_card.is_revealed is True
        assert second_card.is_revealed is True
        assert first_card.is_matched is True
        assert second_card.is_matched is True

    # Step 3
    def test_card_matching_invalid_reset(self, sample_board):
        # Get first two cards
        first_card = sample_board.cards[0]
        second_card = sample_board.cards[1]
        # Flip the cards
        first_card.flip_card()
        second_card.flip_card()
        # Add them to a list to check for a pair
        sample_board.flipped_cards = [first_card, second_card]
        sample_board.check_match()
        # Since they dont match check if card resets
        assert first_card.is_revealed is False
        assert second_card.is_revealed is False
        assert first_card.is_matched is False
        assert second_card.is_matched is False
    

# UT_03
