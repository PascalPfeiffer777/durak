import random

from core.card import Card, CARD_COLORS, CARD_VALUES


def generate_random_card():
    return Card(random.sample(CARD_VALUES, 1)[0], random.sample(CARD_COLORS, 1)[0])


def gen_card_deck():
    return [Card(v,c) for v in CARD_VALUES for c in CARD_COLORS]


def iterate_cards(players):
    for p in players:
        for c in p.hand:
            yield c


def deal_starting_hand(players, cards):
    random.shuffle(cards)
    for _ in range(6):
        for p in players:
            p.draw_card(cards.pop())
    print('Cards have been dealt.')


def draw_trump_card(cards):
    trump = cards.pop()
    cards.insert(0, trump)
    print(f'{trump.color.capitalize()} is trump!')
    return trump.color


def determine_starting_player(players):
    beginner = sorted(players, key=lambda x: [
                      y for y in x.hand if y.is_trump])[0]
    beginner.start_turn()
    #determine_positions(players) 
    print(f'{beginner.name} starts the game.')

def make_trumps(players, trump):
    for card in iterate_cards(players):
        if card.color == trump:
            card.make_trump()


def determine_positions(players):
    r_players = players[::-1]
    attacker =  next(p for p in r_players if p.is_attacker==True)
    attacker_index = r_players.index(attacker)
    r_players[attacker_index -1].is_defender = True
    r_players[attacker_index].is_neighbour = True
    r_players[attacker_index - 2].is_neighbour = True
    print(f'Neighbours: {[p.name for p in players if p.is_neighbour]}')


def play_attack(players, table_cards):
    attacker =  next(p for p in players if p.is_attacker==True) 
    card = attacker.play_random_card()
    defender =  next(p for p in players if p.is_defender==True) 
    print(f'{attacker.name} played {card} on {defender.name}.')
    table_cards.append(card)


def next_players_turn(players):
    pass