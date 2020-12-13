class Table(list):
    def __init__(self, players):
        super().__init__(self)
        self.players = players

    def append(self, e):
        super().append(e)
        print(f'Cards on the table: {self}.')
        for p in self.players:
            p.play_cards_to_neigbhour(self)