from itertools import cycle
from core.game_logic import (
                       gen_card_deck,
                       deal_starting_hand,
                       draw_trump_card,
                       make_trumps,
                       determine_starting_player
                       )

from core.player import Player
 
def main():
    player_names = ['Carlos', 'Mike', 'Andreas', 'Pascal']
    players = [Player(name) for name in player_names]
    cards = gen_card_deck()
    table_cards = []
    deal_starting_hand(players, cards)
    trump = draw_trump_card(cards)
    make_trumps(players, trump)
    determine_starting_player(players)
    active_player = next(p for p in players if p._is_turn)
    order = cycle(players)
    while True:
        left_neighbour, right_neibghour = None
        card = active_player.play_random_card()
        table_cards.append(card)


        


    
    