class Table(list):
    def __init__(self, players):
        super().__init__(self)
        self.players = players

    def append(self, e):
        super().append(e)
        print(f'Cards on the table: {self}.')
        for p in self.players:
            p.play_cards_to_neigbhour(self)
            p.play_defense(self)

    def determine_positions(self):
        r_players = self.players[::-1]
        attacker =  next(p for p in r_players if p.is_attacker==True)
        attacker_index = r_players.index(attacker)
        r_players[attacker_index -1].is_defender = True
        r_players[attacker_index].is_neighbour = True
        r_players[attacker_index - 2].is_neighbour = True
        print(f'Neighbours: {[p.name for p in self.players if p.is_neighbour]}')
        for p in r_players:
            p.defending_player = r_players[attacker_index -1]
            p.right_neigbhour = r_players[r_players.index(p) - 1]
