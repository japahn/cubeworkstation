class CardPile(object):
    def __init__(self, cards):
        self._cards = list(cards)
        self._string_repr = None

    def cards(self):
        return self._cards

    def size(self):
        return len(self._cards)

    def __str__(self):
        if self._string_repr is None:
            self._string_repr = '-- Booster --\n'
            for card in self._cards:
                self._string_repr += str(card) + '\n'
            self._string_repr += '-- end --'
        return self._string_repr
