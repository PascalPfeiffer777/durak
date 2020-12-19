from core.game_logic import (
                       gen_card_deck,
                       play_attack 
                       )

from core.player import Player
from core.table import Table
 
def main():
    player_names = ['Carlos', 'Mike', 'Andreas', 'Pascal']
    players = [Player(name) for name in player_names]
    deck = gen_card_deck()
    table = Table(players=players, deck=deck)
    for p in players:
        p.join_table(table)


    table.deal_starting_hand()
    table.draw_trump_card()
    table.make_trumps()
    table.determine_starting_player()
    while True:
        play_attack(players, table) 
        import time; time.sleep(2)

        
if __name__ == "__main__":
    main()


        


    
    