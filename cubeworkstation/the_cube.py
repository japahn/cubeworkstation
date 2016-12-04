from card_pile import CardPile
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
            module = MODULES[module_name]
            for pool in module.values():
                cube.add_section(pool)
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

        return all_boosters

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
            all_boosters.append(big_pile.draw_cards(15))

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
