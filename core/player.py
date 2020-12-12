import random

class Player:
    def __init__(self, name):
        self.name = name
        self._is_turn = False
        self._under_attack = False
        self._can_attack = False
        self.hand = []


    def start_turn(self):
        self._is_turn = True
        self._can_attack = True

    def end_turn(self):
        self._is_turn = False

    def draw_card(self, card):
        self.hand.append(card)

    def determine_possible_moves(self, table_cards):
        if self._is_turns & self._can_attack:
            # can play each single card
            # can play multiple cards
            pass

    def play_random_card(self):
        return self.hand.pop(random.randint(0,len(self.hand)))


    def play_cards(self):
        pass

    def pick_up_cards(self, table_cards):
        pass

    def cover_cards(self, table_cards):
        pass

    def attack_neighour(self):
        pass


    def __repr__(self):
        return f'Payer(name={self.name})'