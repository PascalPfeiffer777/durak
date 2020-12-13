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
    print(f'{beginner.name} starts the game.')

def make_trumps(players, trump):
    for card in iterate_cards(players):
        if card.color == trump:
            card.make_trump()


def draw_cards(players, cards):
    while min([len(p.hand) for p in players]) < 6:
        for p in players:
            # TODO: Make sure drawing is in the right order!
            p.draw_card(cards.pop())
            if not cards:
                break

def determine_neibghours(players):
    defender =  next(p for p in players if p._is_defender==True)
    defender_index = players.index(defender)
    right_neibour, left_neighbour =  defender_index + 1, defender_index - 1 
    players[left_neighbour]._is_neighbour = True
    try: 
        players[right_neibour]._is_neighbour = True
    except IndexError:
        players[0]._is_neighbour = True
    print(f'Neighbours: {[p.name for p in players if p._is_neighbour]}')

def play_attack(players, table_cards):
    attacker =  next(p for p in players if p._is_turn==True) 
    card = attacker.play_random_card()
    attacker_index = players[::-1].index(attacker)
    defender =  players[::-1][attacker_index -1]
    defender._is_defender=True
    print(f'{attacker.name} played {card} on {defender.name}.')
    table_cards.append(card)

def play_defense(players, table_cards):
    pass #TODO: Probably a good place to continue :)
    # try to forward
    # try to cover
    # pick up cards

