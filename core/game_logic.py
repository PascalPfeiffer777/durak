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

def play_attack(players, table_cards):
    attacker =  next(p for p in players if p.is_attacker==True) 
    card = attacker.play_random_card()
    defender =  next(p for p in players if p.is_defender==True) 
    print(f'{attacker.name} played {card} on {defender.name}.')
    attacker.check_victory()
    table_cards.append(card)
