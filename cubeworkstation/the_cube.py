from cube_data import build_cube

class TheCube(object):
    def __init__(self):
        self.cube = build_cube()

    def make_boosters_for_players(self, num_players):
        all_boosters = []

        main_pile = self.cube.sections()['mod_main'].create_pile()
        main_pile.shuffle()
        lands_pile = self.cube.sections()['mod_lands'].create_pile()
        lands_pile.shuffle()

        for player in xrange(num_players):
            drawn_from_main = main_pile.draw_cards(41)
            drawn_from_lands = lands_pile.draw_cards(4)
            player_pile = (drawn_from_main + drawn_from_lands)
            player_pile.shuffle()
            boosters = player_pile / 3
            all_boosters.extend(boosters)

        return all_boosters
