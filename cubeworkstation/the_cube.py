from booster_building import build_boosters_from_recipe_by_player
from card_pile import CardPile
from cube import Cube
from cube_data import MODULES
from cube_module import CubeModule
from mtgjson import (SECTION_W, SECTION_U, SECTION_B, SECTION_R, SECTION_G, SECTION_OTHER, ALL_SECTIONS)

class TheCube(object):
    def __init__(self):
        self._cube = self.build_cube()

    @staticmethod
    def build_cube():
        cube = Cube()
        cube_modules = [
            'mod_lands',
            'mod_lands_simple',
            'mod_main',
            'mod_simple',
            'rare',
        ] + ['module%d' % (i + 1) for i in xrange(4)]
        for module_name in cube_modules:
            cube.add_module(MODULES[module_name])

        mod_main_without_rares = CubeModule.subtract('mod_main_without_rares',
                                                     MODULES['mod_main'],
                                                     MODULES['rare'])
        cube.add_module(mod_main_without_rares)

        mod_lands_without_simple = CubeModule.subtract('mod_lands_without_simple',
                                                     MODULES['mod_lands'],
                                                     MODULES['mod_lands_simple'])
        cube.add_module(mod_lands_without_simple)

        return cube

    def cube(self):
        return self._cube

    def good_stuff_draft(self, num_players):
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

    def rare_draft(self, num_players):
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

        rare_pile = self._cube.modules()['rare'].pool().create_pile()
        rare_pile.shuffle()
        for booster in all_boosters:
            rare = rare_pile.draw_card()
            booster.add_top(rare)

        return all_boosters

    def simple_draft(self, num_players):
        RECIPE_PER_PLAYER = {
            ('mod_simple', SECTION_W): 7,
            ('mod_simple', SECTION_U): 7,
            ('mod_simple', SECTION_B): 7,
            ('mod_simple', SECTION_R): 7,
            ('mod_simple', SECTION_G): 7,
            ('mod_simple', SECTION_OTHER): 6,
            ('mod_lands_simple', SECTION_OTHER): 4,
        }

        return build_boosters_from_recipe_by_player(self._cube, RECIPE_PER_PLAYER, num_players)

    # simplicity is [0.0, 1.0], where:
    #     0.0 is equal to good_stuff_draft()
    #     1.0 is equal to simple_draft()
    def partially_simple_draft(self, num_players, simplicity):
        assert simplicity >= 0.0
        assert simplicity <= 1.0

        SPELLS_PER_PLAYER = {
            SECTION_W: 7,
            SECTION_U: 7,
            SECTION_B: 7,
            SECTION_R: 7,
            SECTION_G: 7,
            SECTION_OTHER: 6,
        }
        LANDS_PER_PLAYER = 4

        piles = {}
        for color in ALL_SECTIONS:
            for module in ['mod_main', 'mod_simple']:
                section_id = (module, color)
                pile = self._cube.sections()[section_id].create_pile()
                pile.shuffle()
                piles[section_id] = pile

        for module in ['mod_lands_simple', 'mod_lands_without_simple']:
            section_id = (module, SECTION_OTHER)
            pile = self._cube.sections()[section_id].create_pile()
            pile.shuffle()
            piles[section_id] = pile

        for color in ALL_SECTIONS:
            cards_total, cards_from_simple, cards_from_main = self._card_mixed_distribution(
                num_players, SPELLS_PER_PLAYER[color], simplicity)

            piles[color] = (piles[('mod_main', color)].draw_cards(cards_from_main)
                            + piles[('mod_simple', color)].draw_cards(cards_from_simple))
            piles[color].shuffle()

        cards_total, cards_from_simple, cards_from_main = self._card_mixed_distribution(
            num_players, LANDS_PER_PLAYER, simplicity)
        piles['lands'] = (piles[('mod_lands_without_simple', color)].draw_cards(cards_from_main)
                          + piles[('mod_lands_simple', color)].draw_cards(cards_from_simple))
        piles['lands'].shuffle()

        all_boosters = []
        for _ in xrange(num_players):
            player_pile = CardPile.empty()
            for color in ALL_SECTIONS:
                player_pile += piles[color].draw_cards(SPELLS_PER_PLAYER[color])
            player_pile += piles['lands'].draw_cards(LANDS_PER_PLAYER)
            player_pile.shuffle()

            all_boosters.extend(player_pile / 3)

        for booster in all_boosters:
            booster.sort_by_section()

        return all_boosters

    def _card_mixed_distribution(self, num_players, cards_per_player, simplicity):
        cards_total = cards_per_player * num_players
        cards_from_simple = int(simplicity * cards_total)
        cards_from_main = cards_total - cards_from_simple
        return cards_total, cards_from_simple, cards_from_main

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
