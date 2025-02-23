import pytest
from src.board import Board

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

# Matching term board
@pytest.fixture
def matching_sample_board(matching_pair_terms):
    matching_board = Board(800, 600)
    matching_board.create_grid(terms=matching_pair_terms, cols=4, rows=3)
    return matching_board

# Empty terms
@pytest.fixture
def zero_terms():
    return []

# Empty terms board
@pytest.fixture
def zero_terms_board(zero_terms):
    zero_board = Board(800,600)
    zero_board.create_grid(terms=zero_terms, cols=4, rows=3)
    return zero_board

# UT_01
class TestUT01:
    # Step 1
    def test_number_of_cards(self, sample_board):
        assert sample_board.width == 800
        assert sample_board.height == 600
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
            if card.term not in unique_acro:
                unique_acro.append(card.term)
                # Adds 1 to the counter aswell as the card counter
                term_count += 1
                card_count += 1
            else:
                card_count += 1

        # There should be 16 cards with 8 terms, therefore the rest of the 8 terms have been doubled
        assert card_count == 16
        assert term_count == 8
    
    # Step 4
    def test_start_game_with_no_cards(self, zero_terms_board):
        assert len(zero_terms_board.cards) == 0