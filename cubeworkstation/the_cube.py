from cube import Cube
from card_pile import CardPile
from cube_data import build_cube
from util import grouper

class TheCube(object):
    def __init__(self):
        self.cube = build_cube()

    def make_boosters(self, num_boosters):
        main_section = self.cube.sections()['mod_main']
        drawn_from_main = main_section.draw_cards(num_boosters * 15)
        cards_grouped_by_booster = grouper(15, drawn_from_main)

        return [CardPile('Booster', b) for b in cards_grouped_by_booster]
