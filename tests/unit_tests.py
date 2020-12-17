from core.card import Card
from core.player import Player
from core.game_logic import gen_card_deck, iterate_cards 

def test_if_card_has_higher_value():
    heart_king = Card(13, 'heart')
    heart_six = Card(6, 'heart')
    assert heart_king > heart_six

def test_if_card_has_same_value():
    heart_seven = Card(7, 'heart')
    spade_seven = Card(7, 'spade')
    assert heart_seven == spade_seven

def test_if_color_matches():
    heart_seven = Card(7, 'heart')
    heart_six = Card(6, 'heart')
    assert heart_seven._matches_color(heart_six)

def test_if_lower_trump_wins():
    heart_six = Card(6,'heart')
    heart_seven = Card(7, 'heart')
    heart_six.make_trump()
    assert heart_six > heart_seven

def test_if_lower_trump_loses():
    heart_six = Card(6,'heart')
    heart_seven = Card(7, 'heart')
    heart_six.make_trump()
    heart_seven.make_trump()
    assert (heart_six > heart_seven) == False

def test_len_card_deck():
    assert len(gen_card_deck()) == 36


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


test_if_card_has_higher_value()
test_if_card_has_same_value()
test_if_color_matches()
test_if_lower_trump_wins()
test_if_lower_trump_loses()
test_len_card_deck()
test_player_can_cover_cards()
test_player_cant_cover_cards()
test_player_can_cover_cards_with_trump()
test_player_cant_cover_cards_with_trump()