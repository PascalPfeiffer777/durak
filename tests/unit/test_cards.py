from core.card import Card
from core.game_logic import gen_card_deck 

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

