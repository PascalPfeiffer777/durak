import random

class Player:
    def __init__(self, name):
        self.name = name
        self._is_attacker = False 
        self._is_defender = False
        self.is_neighbour = False 
        self.hand = []
        self.defending_player = None #type: Player
        self.right_neigbhour = None #type: Player

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
        self.table.determine_positions()


    def join_table(self, table):
        self.table = table


    def start_turn(self):
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


    def play_card(self, card, table_cards):
        self.hand.remove(card)
        table_cards.append(card)

    def pick_up_cards(self, table_cards):
        pass

    def cover_cards(self, table_cards):
        pass

    def attack_neighour(self):
        pass

    def forward_cards(self, value, table_cards):
        card = next(v for v in self.hand if v.value == value)
        self.play_card(card, table_cards)
        self.is_attacker = True 


    def play_cards_to_neigbhour(self, table_cards):
        if self.is_neighbour == True:
            for card in self.hand:
                if (card.value in [c.value for c in table_cards]) & (len(table_cards) < 7) & (len(self.defending_player.hand) > len(table_cards)):
                    print(f'{self.name} added a {card} to the table_cards.')
                    self.play_card(card, table_cards)
                     
    def play_defense(self, table_cards):
        if self._is_defender != True:
            return
        unique_values = list(set(v.value for v in table_cards))  
        if (len(unique_values)==1) & (unique_values[0] in [c.value for c in self.hand]) & (len(table_cards) + 1 <= len(self.right_neigbhour.hand)):
            self.forward_cards(value=unique_values[0], table_cards=table_cards)
        else:
            self.cover_cards(table_cards)


    def __repr__(self):
        return f'Player(name={self.name})'