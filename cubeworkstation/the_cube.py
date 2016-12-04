from booster_building import build_boosters_from_recipe_by_player
from cube import Cube
from cube_data import MODULES
from mtgjson import (SECTION_W, SECTION_U, SECTION_B, SECTION_R, SECTION_G, SECTION_OTHER)

class TheCube(object):
    def __init__(self):
        self._cube = self.build_cube()

    @staticmethod
    def build_cube():
        cube = Cube()
        cube_modules = [
            'mod_lands',
            'mod_main',
            'mod_simple'
        ] + ['module%d' % (i + 1) for i in xrange(4)]
        for module_name in cube_modules:
            cube.add_module(MODULES[module_name])
        return cube

    def cube(self):
        return self._cube

    def good_stuff_draft(self, num_players):
        all_boosters = []

        RECIPE_PER_PLAYER = {
            ('mod_main', SECTION_W): 7,
            ('mod_main', SECTION_U): 7,
            ('mod_main', SECTION_B): 7,
            ('mod_main', SECTION_R): 7,
            ('mod_main', SECTION_G): 7,
            ('mod_main', SECTION_OTHER): 6,
            ('mod_lands', SECTION_OTHER): 4,
        }

        return build_boosters_from_recipe_by_player(self._cube, RECIPE_PER_PLAYER, num_players)

    def full_random_draft(self, num_players):
        LANDS_SECTION = ('mod_lands', SECTION_OTHER)
        SPELL_SECTIONS = [
            ('mod_main', SECTION_W),
            ('mod_main', SECTION_U),
            ('mod_main', SECTION_B),
            ('mod_main', SECTION_R),
            ('mod_main', SECTION_G),
            ('mod_main', SECTION_OTHER),
        ]

        big_pile = self._cube.sections()[LANDS_SECTION].create_pile().draw_cards(40)
        for section_name in SPELL_SECTIONS:
            pile = self._cube.sections()[section_name].create_pile()
            big_pile += pile
        big_pile.shuffle()

        all_boosters = []
        for _ in xrange(num_players * 3):
            booster = big_pile.draw_cards(15)
            booster.sort_by_section()
            all_boosters.append(booster)

        return all_boosters

if __name__ == '__main__':
    the_cube = TheCube()
    sections = the_cube.cube().sections()
    section_names_sorted = sorted(sections.keys())
    for section_name in section_names_sorted:
        section = sections[section_name]
        print section
        print
    print the_cube.cube()
