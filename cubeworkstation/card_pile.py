from random import sample

class CardPile(object):

    def __init__(self, name, cards):
        self._pile_name = name
        self._cards = list(cards)
        self._string_repr = None

    def name(self):
        return self._pile_name

    def cards(self):
        return self._cards

    def size(self):
        return len(self._cards)

    def draw_cards(self, num_cards):
        return sample(self.cards(), num_cards)

    def __str__(self):
        if self._string_repr is None:
            self._string_repr = '-- %s (%d) --\n' % (self._pile_name, self.size())
            for card in self._cards:
                self._string_repr += str(card) + '\n'
            self._string_repr += '-- end --'
        return self._string_repr
