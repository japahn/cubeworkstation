from card_pile import CardPile


def build_boosters_from_recipe_by_player(cube, recipe, num_players):
    piles = {}
    for section_name, _ in recipe.iteritems():
        pile = cube.sections()[section_name].create_shuffled_pile()
        piles[section_name] = pile

    all_boosters = []
    for player in xrange(num_players):
        player_pile = CardPile.empty()
        for section_name, num_from_section in recipe.iteritems():
            section_pile = piles[section_name]
            drawn = section_pile.draw_cards(num_from_section)
            player_pile += drawn
        player_pile.shuffle()
        boosters = player_pile / 3
        all_boosters.extend(boosters)

    for i, booster in enumerate(all_boosters):
        booster.rename('Booster %d' % (i + 1))
        booster.sort_by_section()

    return all_boosters
