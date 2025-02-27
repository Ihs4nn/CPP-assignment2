import pytest
from src.main import GameScreen

@pytest.fixture
# Matching terms
def matching_pair_terms():
    return [
        ("ADO", "Azure DevOps - software suite for tracking/deploying")
    ]

@pytest.fixture
def matching_game(matching_pair_terms):
    gs = GameScreen(800, 600)
    gs.game.terms = matching_pair_terms
    gs.game.board.create_grid(terms=matching_pair_terms, cols=1, rows=2)
    gs.game.board.flipped_cards = []
    return gs


# RT_01
class TestRT01:
    # Step 1
    def test_flip_single_card(matching_game_screen):
        # Get a card from the board
        card = matching_game_screen.game.board.cards[0]
        # Check its inital state is hidden
        assert card.is_revealed == False
        # Simulate a click from the user
        matching_game_screen.game.handle_card_click(card)
        # Check it now becomes revealed
        assert card.is_revealed == True
    # Step 2
    def test_matching_cards(matching_game_screen):
        board = matching_game_screen.game.board
        # Gets the first and second card from the board
        first_card = board.cards[0], 
        second_card = board.cards[1]
        # Imitates user clicking
        matching_game_screen.game.handle_card_click(first_card)
        matching_game_screen.game.handle_card_click(second_card)
        # Now that the UI has a delay, subtract delay time
        matching_game_screen.game.wait_start_time -= matching_game_screen.game.wait_delay
        # Update the screen
        matching_game_screen.game.update_flip()
        # Check that the card are matched and revealed
        assert first_card.is_revealed is True
        assert second_card.is_revealed is True
        assert first_card.is_matched is True
        assert second_card.is_matched is True
        # Check that the list clears after a handle_click
        assert len(board.flipped_cards) == 0
    # Step 3
    def test_flip_matched_card(matching_game_screen):
        board = matching_game_screen.game.board
        first_card = board.cards[0], 
        second_card = board.cards[1]
        matching_game_screen.game.handle_card_click(first_card)
        matching_game_screen.game.handle_card_click(second_card)
        matching_game_screen.game.wait_start_time -= matching_game_screen.game.wait_delay
        matching_game_screen.game.update_flip()
        # Gets the state which should be revealed
        state = first_card.is_revealed
        matching_game_screen.game.handle_card_click(first_card)
        # Makes sure the state is the same even if it is clicked
        assert first_card.is_revealed == state
        # Verifies its still matched even if clicked again
        assert first_card.is_matched is True