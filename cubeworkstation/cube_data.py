from collections import defaultdict

from card import Card
from card_pool import CardPool
from cube import Cube
import mtgjson

_MODULES = {}
_MODULES['mod_lands'] = 'data/mod_lands.txt'
_MODULES['mod_main'] = 'data/mod_main.txt'
_MODULES['mod_simple'] = 'data/mod_simple.txt'
_MODULES['module1'] = 'data/module1.txt'
_MODULES['module2'] = 'data/module2.txt'
_MODULES['module3'] = 'data/module3.txt'
_MODULES['module4'] = 'data/module4.txt'

def read_text_pool(module_name, file_name):
    card_pools = {}

    with file(file_name) as f:
        lines = f.readlines()
    lines = map(lambda s: s.strip(), lines)
    cards = map(lambda s: Card(s), lines)
    cards_by_section = defaultdict(list)
    for card in cards:
        section = mtgjson.get_section(card.name())
        cards_by_section[section].append(card)

    for section_id, section_cards in cards_by_section.iteritems():
        section_name = '%s - Section %s' % (module_name, section_id)
        card_pool = CardPool(section_name, section_cards)
        card_pools[section_name] = card_pool

    return card_pools

def build_cube():
    cube = Cube()
    for module_name, module_file in _MODULES.iteritems():
        pools = read_text_pool(module_name, module_file)
        for pool in pools.values():
            cube.add_section(pool)
    return cube

if __name__ == '__main__':
    cube = build_cube()
    sections = cube.sections()
    section_names_sorted = sorted(sections.keys())
    for section_name in section_names_sorted:
        section = sections[section_name]
        print section
        print
    print cube
