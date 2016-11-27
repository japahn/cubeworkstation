from card_pile import CardPile
from cube_data import build_cube

class TheCube(object):
    def __init__(self):
        self.cube = build_cube()

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
            pile = self.cube.sections()[section_name].create_pile()
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
