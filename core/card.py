import functools

@functools.total_ordering
class Card():
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.is_trump = False

        self._face_matching = {11:'Jack',
                          12:'Queen',
                          13:'King',
                          14: 'Ace'}

    def make_trump(self):
        "Makes a card to a trump card at the beginning of a round."
        self.is_trump = True

    def _matches_color(self,other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.color == other.color

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        return self.value == other.value

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError
        elif (self.is_trump == True) & (other.is_trump == False):
            return True
        else:
            return self.value >= other.value

    def __repr__(self):
        val = self.value if self.value not in self._face_matching.keys() else self._face_matching.get(self.value)
        return f'Card({val}, {self.color}, trump={self.is_trump})'

CARD_VALUES = [i for i in range(6,15)]
CARD_COLORS = ['heart', 'spade', 'club', 'diamond']