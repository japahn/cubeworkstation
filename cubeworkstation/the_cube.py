from card_pile import CardPile
from cube_data import build_cube

class TheCube(object):
    def __init__(self):
        self._cube = build_cube()

    def good_stuff_draft(self, num_players):
        all_boosters = []

        RECIPE_PER_PLAYER = {
            'mod_main - Section 1. W': 7,
            'mod_main - Section 2. U': 7,
            'mod_main - Section 3. B': 7,
            'mod_main - Section 4. R': 7,
            'mod_main - Section 5. G': 7,
            'mod_main - Section 6. Other': 6,
            'mod_lands - Section 6. Other': 4,
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
        LANDS_SECTION = 'mod_lands - Section 6. Other'
        SPELL_SECTIONS = [
            'mod_main - Section 1. W',
            'mod_main - Section 2. U',
            'mod_main - Section 3. B',
            'mod_main - Section 4. R',
            'mod_main - Section 5. G',
            'mod_main - Section 6. Other',
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

    def cube(self):
        return self._cube
