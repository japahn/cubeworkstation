from collections import defaultdict

from card_pool import CardPool
import mtgjson

class CubeModule(object):

    def __init__(self, module_name, cards):
        self._module_name = module_name
        self._sections = {}
        self._pool = CardPool(module_name, cards)

        cards_by_section = defaultdict(list)
        for card in cards:
            color = mtgjson.get_section(card.name())
            cards_by_section[color].append(card)

        for color, section_cards in cards_by_section.iteritems():
            section_id = (module_name, color)
            card_pool = CardPool(section_id, section_cards)
            self._sections[section_id] = card_pool
            for card in section_cards:
                card.set_section(section_id)

    def name(self):
        return self._module_name

    def all_sections(self):
        return self._sections.values()

    def rename(self, new_name):
        old_name = self._module_name
        self._module_name = new_name
        for card in self.all_cards():
            card.module_was_renamed(old_name, new_name)

    def all_cards(self):
        all_cards = []
        for section in self.all_sections():
            all_cards.extend(section.cards())
        return all_cards

    def pool(self):
        return self._pool

    @classmethod
    def subtract(cls, new_name, first, second):
        my_cards = first.all_cards()
        their_cards = second.all_cards()

        new_cards = list(my_cards)
        for their_card in their_cards:
            for new_card in new_cards:
                if new_card.name() == their_card.name():
                    new_cards.remove(new_card)
                    break

        return CubeModule(new_name, new_cards)
