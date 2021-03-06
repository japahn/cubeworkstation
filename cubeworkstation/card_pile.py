from random import sample

class CardPile(object):

    def __init__(self, name, cards):
        self._pile_name = name
        self._cards = list(cards)

    @classmethod
    def empty(cls):
        return cls('Empty', [])

    def name(self):
        return self._pile_name

    def cards(self):
        return self._cards

    def size(self):
        return len(self._cards)

    def rename(self, new_name):
        self._pile_name = new_name

    def shuffle(self):
        self._cards = sample(self._cards, len(self._cards))

    def sort_by_section(self):
        self._cards.sort(key=lambda c: min(c.sections()))

    def draw_cards(self, num_cards, name=None):
        assert (self.size() >= num_cards), ('Trying to draw %d cards from pile %s with %d cards' %
            (num_cards, self.name(), self.size()))
        drawn_cards = self._cards[:num_cards]
        del self._cards[:num_cards]
        return CardPile(name if name else 'Drawn', drawn_cards)

    def draw_card(self):
        return self._cards.pop(0)

    def add_top(self, card):
        self._cards.insert(0, card)

    def __add__(self, other):
        name = '(%s + %s)' % (self.name(), other.name())
        cards = self.cards() + other.cards()
        return CardPile(name, cards)

    def __div__(self, denominator):
        assert (self.size() % denominator == 0), ('Cannot divide CardPile of size %d by %d' %
            (self.size(), denominator))
        cards_per_pile = self.size() / denominator

        all_piles = []

        for i in xrange(denominator):
            piece_i = i + 1
            name = '(%s piece %d/%d)' % (self.name(), piece_i, denominator)
            pile = self.draw_cards(cards_per_pile, name)
            all_piles.append(pile)
        return all_piles

    def __str__(self):
        string_repr = '-- %s (%d) --\n' % (self._pile_name, self.size())
        for card in self._cards:
            string_repr += str(card) + '\n'
        string_repr += '-- end --'
        return string_repr

if __name__ == '__main__':
    pile = CardPile('test', range(10))
    assert pile.size() == 10

    pile.shuffle()

    drawn3 = pile.draw_cards(3)
    assert pile.size() == 7
    assert drawn3.size() == 3

    drawn2 = pile.draw_cards(2)
    assert pile.size() == 5
    assert drawn2.size() == 2

    print 'OK'
