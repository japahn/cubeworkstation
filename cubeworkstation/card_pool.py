from card_pile import CardPile

class CardPool(object):

    def __init__(self, name, cards):
        self._pool_name = name
        self._cards = list(cards)
        self._string_repr = None

    def name(self):
        return self._pool_name

    def cards(self):
        return self._cards

    def size(self):
        return len(self._cards)

    def create_pile(self):
        return CardPile(self._pool_name, self._cards)

    def __str__(self):
        if self._string_repr is None:
            self._string_repr = '-- POOL %s (%d) --\n' % (self._pool_name, self.size())
            for card in self._cards:
                self._string_repr += str(card) + '\n'
            self._string_repr += '-- end --'
        return self._string_repr
