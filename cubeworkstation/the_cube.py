from cube import Cube
from card_pile import CardPile

class TheCube(object):
    def __init__(self):
        self.cube = Cube()

    def make_boosters(self, num_boosters):
        return [CardPile([]) for _ in xrange(num_boosters)]
