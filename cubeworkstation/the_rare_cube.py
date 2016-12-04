from card_pile import CardPile
from cube import Cube
from cube_data import MODULES
from cube_module import CubeModule
from mtgjson import (SECTION_W, SECTION_U, SECTION_B, SECTION_R, SECTION_G, SECTION_OTHER)


class TheRareCube(object):
    def __init__(self):
        self._cube = self.build_cube()

    @staticmethod
    def build_cube():
        cube = Cube()

        mod_main_without_rares = CubeModule.subtract('mod_main_without_rares',
                                                     MODULES['mod_main'],
                                                     MODULES['rares_in_main'])

        cube.add_module(mod_main_without_rares)
        cube.add_module(MODULES['mod_lands'])
        cube.add_module(MODULES['rares_in_main'])
        return cube

    def cube(self):
        return self._cube

    def good_stuff_draft(self, num_players):
        all_boosters = []

        RECIPE_PER_PLAYER = {
            ('mod_main_without_rares', SECTION_W): 6,
            ('mod_main_without_rares', SECTION_U): 6,
            ('mod_main_without_rares', SECTION_B): 6,
            ('mod_main_without_rares', SECTION_R): 6,
            ('mod_main_without_rares', SECTION_G): 6,
            ('mod_main_without_rares', SECTION_OTHER): 6,
            ('mod_lands', SECTION_OTHER): 6,
        }

        piles = {}
        for section_name, _ in RECIPE_PER_PLAYER.iteritems():
            pile = self._cube.sections()[section_name].create_pile()
            pile.shuffle()
            piles[section_name] = pile

        for player in xrange(num_players):
            player_pile = CardPile.empty()
            for section_name, num_from_section in RECIPE_PER_PLAYER.iteritems():
                section_pile = piles[section_name]
                drawn = section_pile.draw_cards(num_from_section)
                player_pile += drawn
            player_pile.shuffle()
            boosters = player_pile / 3
            all_boosters.extend(boosters)

        for i, booster in enumerate(all_boosters):
            booster.rename('Booster %d' % (i + 1))
            booster.sort_by_section()

        rare_pile = self._cube.modules()['rares_in_main'].pool().create_pile()
        rare_pile.shuffle()
        for booster in all_boosters:
            rare = rare_pile.draw_card()
            booster.add_top(rare)

        return all_boosters

if __name__ == '__main__':
    the_cube = TheRareCube()
    sections = the_cube.cube().sections()
    section_names_sorted = sorted(sections.keys())
    for section_name in section_names_sorted:
        section = sections[section_name]
        print section
        print
    print the_cube.cube()
