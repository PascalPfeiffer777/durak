import random
from .game_logic import iterate_cards

class Table(list):
    def __init__(self, players, deck):
        super().__init__(self)
        self.players = players
        self.deck = deck

    def append(self, e):
        super().append(e)
        print(f'Cards on the table: {self}.')
        for p in self.players:
            p.play_cards_to_neigbhour(self)
            p.play_defense(self)


    def deal_starting_hand(self):
        random.shuffle(self.deck)
        for _ in range(6):
            for p in self.players:
                p.draw_card(self.deck.pop())
        print('Cards have been dealt.')


    def draw_trump_card(self):
        trump = self.deck.pop()
        self.deck.insert(0, trump)
        print(f'{trump.color.capitalize()} is trump!')
        return trump.color


    def determine_starting_player(self):
        beginner = sorted(self.players, key=lambda x: [
                        y for y in x.hand if y.is_trump])[0]
        beginner.start_turn() 
        print(f'{beginner.name} starts the game.')

    def make_trumps(self):
        for card in iterate_cards(self.players):
            if card.color == self.deck[0].color:
                card.make_trump()

    def reset_positions(self):
        for p in self.players:
            p.is_attacker = False
            p.is_defender = False
            p.is_neighbour = False
            p._started_defending = False

    def determine_positions(self):
        r_players = self.players[::-1]
        attacker =  next(p for p in r_players if p.is_attacker==True)
        attacker_index = r_players.index(attacker)
        r_players[attacker_index -1].is_defender = True
        r_players[attacker_index].is_neighbour = True
        r_players[attacker_index - 2].is_neighbour = True
        for p in r_players:
            p.defending_player = r_players[attacker_index -1]
            p.right_neigbhour = r_players[r_players.index(p) - 1]

    def draw_cards_after_round(self):
        for p in self.players:
            while (len(p.hand) < 6) & (len(self.deck) > 0):
                p.draw_card(self.deck.pop())
                