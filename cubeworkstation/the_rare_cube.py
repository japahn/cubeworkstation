from booster_building import build_boosters_from_recipe_by_player
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

        RECIPE_PER_PLAYER = {
            ('mod_main_without_rares', SECTION_W): 6,
            ('mod_main_without_rares', SECTION_U): 6,
            ('mod_main_without_rares', SECTION_B): 6,
            ('mod_main_without_rares', SECTION_R): 6,
            ('mod_main_without_rares', SECTION_G): 6,
            ('mod_main_without_rares', SECTION_OTHER): 6,
            ('mod_lands', SECTION_OTHER): 6,
        }

        all_boosters = build_boosters_from_recipe_by_player(self._cube, RECIPE_PER_PLAYER, num_players)

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
