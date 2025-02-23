import pytest
from src.board import Board
from src.card import Card
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
        assert card.is_revealed == False
        assert card.is_matched == False
    # Step 2
    def test_handling_click_logic(self, start_game):
        start_game.start_new_game()
        card = start_game.board.cards[0]
        start_game.handle_card_click(card)
        assert card.is_revealed == True
        assert len(start_game.board.flipped_cards) == 1
    # Step 3
    def test_second_card_different(self, start_game):
        start_game.start_new_game()
        first_card = start_game.board.cards[0]
        second_card = start_game.board.cards[1]
        start_game.handle_card_click(first_card)
        second_card.handle_card_click(second_card)
        assert len(start_game.board.flipped_cards) == 2
        start_game.check_match()
        assert first_card.is_revealed is False
        assert second_card.is_revealed is False
        assert first_card.is_matched is False
        assert second_card.is_matched is False



        
