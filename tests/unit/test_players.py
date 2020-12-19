from core.player import Player
from core.card import Card
from core.game_logic import iterate_cards


def test_player_can_cover_cards():
    player = Player('TestPlayer')
    player.hand = [Card(10, 'heart'), Card(11, 'heart'), Card(10, 'spade')]
    table_cards = [Card(8, 'heart'), Card(9, 'heart'),Card(8, 'spade')]
    assert player.check_if_cover_is_possible(table_cards)

def test_player_cant_cover_cards():
    player = Player('TestPlayer')
    player.hand = [Card(7, 'heart'), Card(11, 'heart'), Card(10, 'spade')]
    table_cards = [Card(8, 'heart'), Card(9, 'heart'),Card(8, 'spade')]
    assert player.check_if_cover_is_possible(table_cards) == False

def test_player_can_cover_cards_with_trump():
    player = Player('TestPlayer')
    player.hand = [Card(6, 'diamond'), Card(7, 'diamond'), Card(10, 'spade')]
    for card in iterate_cards([player]):
        if card.color == 'diamond': card.make_trump()
    table_cards = [Card(8, 'heart'), Card(9, 'heart'),Card(8, 'spade')]
    assert player.check_if_cover_is_possible(table_cards) 

def test_player_cant_cover_cards_with_trump():
    player = Player('TestPlayer')
    player.hand = [Card(6, 'diamond'), Card(7, 'diamond'), Card(10, 'spade')]
    table_cards = [Card(8, 'heart'), Card(9, 'heart'),Card(8, 'spade')]
    for card in table_cards:
        if card.color == 'heart': card.make_trump()
    assert player.check_if_cover_is_possible(table_cards) == False 

def test_player_can_cover_smaller_number_of_cards():
    player = Player('TestPlayer')
    player.hand = [Card(6, 'diamond'), Card(7, 'diamond'), Card(10, 'spade')]
    table_cards = [Card(8, 'heart')]
    assert player.check_if_cover_is_possible(table_cards) == True
