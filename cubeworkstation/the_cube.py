from cube import Cube
from card_pile import CardPile
from cube_data import build_cube
from util import grouper

class TheCube(object):
    def __init__(self):
        self.cube = build_cube()

    def make_boosters_for_players(self, num_players):
        drawn_from_main = self.cube.sections()['mod_main'].draw_cards(num_players * 45)
        #drawn_from_lands = self.cube.sections()['mod_lands'].draw_cards(num_players * 4)

        cards_grouped_by_booster = grouper(15, drawn_from_main)

        return [CardPile('Booster', b) for b in cards_grouped_by_booster]
