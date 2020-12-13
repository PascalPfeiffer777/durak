import random

class Player:
    def __init__(self, name):
        self.name = name
        self._is_turn = False
        self._is_defender = False
        self._is_atacker = False
        self._is_neighbour = False
        self.hand = []


    def start_turn(self):
        self._is_turn = True
        self._is_atacker = True

    def end_turn(self):
        self._is_turn = False

    def draw_card(self, card):
        self.hand.append(card)

    def determine_possible_moves(self, table_cards):
        if self._is_turns & self._is_atacker:
            # can play each single card
            # can play multiple cards
            pass

    def play_random_card(self):
        return self.hand.pop(random.randint(0,len(self.hand)-1))


    def play_cards(self):
        pass

    def pick_up_cards(self, table_cards):
        pass

    def cover_cards(self, table_cards):
        pass

    def attack_neighour(self):
        pass

    def play_cards_to_neigbhour(self):
        print('I want to play a card now!')


    def __repr__(self):
        return f'Player(name={self.name})'