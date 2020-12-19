import random, sys

class Player:
    def __init__(self, name):
        self.name = name
        self._is_attacker = False 
        self._is_defender = False
        self.is_neighbour = False 
        self.hand = []
        self.defending_player = None #type: Player
        self.right_neigbhour = None #type: Player
        self._self_laid_cards= []
        self._started_defending = False

    @property
    def is_defender(self):
        return self._is_defender

    @is_defender.setter
    def is_defender(self, v):
        self._is_defender = v 

    @property
    def is_attacker(self):
        return self._is_attacker

    @is_attacker.setter
    def is_attacker(self, v):
        self._is_attacker = v 
        if v:
            self.table.determine_positions()


    def join_table(self, table):
        self.table = table


    def start_turn(self):
        self.table.reset_positions()
        self.is_attacker = True
        

    def end_turn(self):
        self.is_attacker = False

    def draw_card(self, card):
        self.hand.append(card)

    def determine_possible_moves(self, table_cards_cards):
        if self._is_turns & self._is_atacker:
            # can play each single card
            # can play multiple cards
            pass

    def play_random_card(self):
        return self.hand.pop(random.randint(0,len(self.hand)-1))

    def check_victory(self):
        if (len(self.hand) == 0) & (len(self.table.deck) == 0):
            print(f'{self.name} won the game!')
            sys.exit()


    def play_card(self, card, table_cards):
        self.hand.remove(card)
        self.check_victory()
        table_cards.append(card)

    def pick_up_cards(self, table_cards):
        while table_cards:
            self.draw_card(table_cards.pop())
        self.table.draw_cards_after_round()
        self._started_defending = False
        print(f'{self.name} picked up the cards.')
        self.right_neigbhour.start_turn()
        

    def check_if_cover_is_possible(self, table_cards):
        possibe = len({v:k for k,v in zip(self.hand, table_cards) if v<k}) == len(table_cards)
        if possibe:
            print(f'{self.name} tries to cover the cards.')
        return possibe

    def covered_cards_succesfully(self):
        print(f'{self.name} covered the cards successfully!')
        self._started_defending = False
        self.table.clear()
        self.table.draw_cards_after_round()
        self.start_turn()

    def cover_cards(self, table_cards):
        cover = {v:k for k,v in zip(self.hand, table_cards) if v<k}
        for card in cover.values():
            self.play_card(card, table_cards=table_cards)
        if set(table_cards).difference(set(cover.values())) != set(cover.keys()):
            for card in cover.values():
                self.hand.append(card)
                table_cards.remove(card)
            if self.check_if_cover_is_possible(table_cards):
                self.cover_cards(table_cards)
            else:
                self.pick_up_cards(table_cards)
        else:
            self.covered_cards_succesfully()
        
    def forward_cards(self, value, table_cards):
        self._started_defending = False
        self.is_defender = False
        self.table.reset_positions()
        self.is_attacker = True    
        card = next(v for v in self.hand if v.value == value)
        print(f'{self.name} forwards the cards to {self.right_neigbhour.name} with a {card}.')
        self.play_card(card, table_cards)
   


    def play_cards_to_neigbhour(self, table_cards):
        if (self.is_neighbour == True) & len(table_cards) > 0:
            for card in self.hand:
                if (card.value in [c.value for c in table_cards]) & (len(table_cards) < 7) & (len(self.defending_player.hand) > len(table_cards)):
                    print(f'{self.name} added a {card} to the table_cards.')
                    self.play_card(card, table_cards)
                     
    def play_defense(self, table_cards):
        if (self._is_defender != True) | (self._started_defending == True) | (len(table_cards) == 0):
            return
        unique_values = list(set(v.value for v in table_cards))  
        if (len(unique_values)==1) & (unique_values[0] in [c.value for c in self.hand]) & (len(table_cards) + 1 <= len(self.right_neigbhour.hand)):
            self.forward_cards(value=unique_values[0], table_cards=table_cards)
        elif self.check_if_cover_is_possible(table_cards):
            self._started_defending = True
            self.cover_cards(table_cards)
        else:
            self.pick_up_cards(table_cards)


    def __repr__(self):
        return f'Player(name={self.name})'