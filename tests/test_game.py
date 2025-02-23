import pytest
from src.board import Board
from src.game import Game

# Creating fixtures
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

@pytest.fixture
def matching_pair_terms():
    return [
        ("ADO", "Azure DevOps - software suite for tracking/deploying")
    ]

@pytest.fixture
def matching_sample_board(matching_pair_terms):
    matching_board = Board(800, 600)
    matching_board.create_grid(terms=matching_pair_terms, cols=4, rows=3)
    return matching_board

@pytest.fixture
def matching_card_game():
    matching_game = Game(800, 600, matching_sample_board)
    return matching_game

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
        # Check if a card is not flipped or matched at the start
        card = start_game.board.cards[0]
        assert card.is_revealed == False
        assert card.is_matched == False

# UT_04
class TestUT04:
    # Step 1
    def test_get_card(self, start_game):
        start_game.start_new_game()
        card = start_game.board.cards[0]
        # Check if the card is initalised properly
        assert card.is_revealed == False
        assert card.is_matched == False
    # Step 2
    def test_handling_click_logic(self, start_game):
        start_game.start_new_game()
        card = start_game.board.cards[0]
        # Calls the clicking function
        start_game.handle_card_click(card)
        # Toggles 'is_revealed' as true 
        assert card.is_revealed == True
        # Appends card to 'flipped_cards' list
        assert len(start_game.board.flipped_cards) == 1
    # Step 3
    def test_second_card_different(self, start_game):
        start_game.start_new_game()
        # Gets first and second card initaised on board
        first_card = start_game.board.cards[0]
        second_card = start_game.board.cards[1]
        # Calls clicking function
        start_game.handle_card_click(first_card)
        start_game.handle_card_click(second_card)
        # Appends cards to the list
        assert len(start_game.board.flipped_cards) == 2
        # Checks if they match
        start_game.check_match()
        # They do not, so will remain as false
        assert first_card.is_revealed is False
        assert second_card.is_revealed is False
        assert first_card.is_matched is False
        assert second_card.is_matched is False
        # Clear list for next round of two clicks
        assert len(start_game.board.flipped_cards) == 0
    # Step 4
    def test_second_card_is_same(self, matching_game):
        # Uses a board with 2 matching cards
        matching_game.start_new_game()
        first_card = matching_game.board.cards[0]
        second_card = matching_game.board.cards[1]
        matching_game.handle_card_click(first_card)
        matching_game.handle_card_click(second_card)
        assert len(matching_game.board.flipped_cards) == 2
        matching_game.check_match()
        # Since they match, the toggles are true
        assert first_card.is_revealed is True
        assert second_card.is_revealed is True
        assert first_card.is_matched is True
        assert second_card.is_matched is True
        # Clears the list for next round
        assert len(matching_game.board.flipped_cards) == 0




        
