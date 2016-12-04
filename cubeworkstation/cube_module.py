from collections import defaultdict

from card_pool import CardPool
import mtgjson

class CubeModule(object):

    def __init__(self, module_name, cards):

        self.sections = {}

        cards_by_section = defaultdict(list)
        for card in cards:
            color = mtgjson.get_section(card.name())
            cards_by_section[color].append(card)

        for color, section_cards in cards_by_section.iteritems():
            section_id = (module_name, color)
            card_pool = CardPool(section_id, section_cards)
            self.sections[section_id] = card_pool
            for card in section_cards:
                card.set_section(section_id)

    def all_sections(self):
        return self.sections.values()
