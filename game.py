from core.game_logic import (
                       determine_neibghours, 
                       gen_card_deck,
                       deal_starting_hand,
                       draw_trump_card,
                       make_trumps,
                       determine_starting_player, play_attack, 
                       )

from core.player import Player
from core.table import Table
 
def main():
    player_names = ['Carlos', 'Mike', 'Andreas', 'Pascal']
    players = [Player(name) for name in player_names]
    cards = gen_card_deck()
    table = Table(players=players)

    deal_starting_hand(players, cards)
    trump = draw_trump_card(cards)
    make_trumps(players, trump)
    determine_starting_player(players)

    play_attack(players, table) 
    determine_neibghours(players)
        
if __name__ == "__main__":
    main()


        


    
    