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

# UT_01
class TestUT01:
    # Step 1
    def test_board_dimensions(self, sample_board):
        assert sample_board.width == 800
        assert sample_board.height == 600

    def test_number_of_cards(self, sample_board):
        # Checks if 16 cards have been created
        assert len(sample_board.cards) == 16
    # Step 2
    def test_if_card_are_hidden(self, sample_board):
        for card in sample_board.cards:
            # Checks the card classes value
            assert card.is_revealed == False
    # Step 3
    def test_each_card_should_have_pair(self, sample_board):
        # Used to count the amount of cards
        card_count = 0
        # Used to count the amount of terms
        term_count = 0
        # List to store unique acroynms found
        unique_acro = []

        for card in sample_board.cards:
            if card.value not in unique_acro:
                unique_acro.append(card.value)
                # Adds 1 to the counter aswell as the card counter
                term_count += 1
                card_count += 1
            else:
                card_count += 1

        # There should be 16 cards with 8 terms, therefore the rest of the 8 terms have been doubled
        assert card_count == 16
        assert term_count == 8

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



