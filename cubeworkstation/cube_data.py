from collections import defaultdict

from card import Card
from card_pool import CardPool
from cube import Cube
import mtgjson

DATA_DIR = 'cubeworkstation/data'

_MODULES = {}
_MODULES['mod_lands'] = '%s/mod_lands.txt' % DATA_DIR
_MODULES['mod_main'] = '%s/mod_main.txt' % DATA_DIR
_MODULES['mod_simple'] = '%s/mod_simple.txt' % DATA_DIR
_MODULES['module1'] = '%s/module1.txt' % DATA_DIR
_MODULES['module2'] = '%s/module2.txt' % DATA_DIR
_MODULES['module3'] = '%s/module3.txt' % DATA_DIR
_MODULES['module4'] = '%s/module4.txt' % DATA_DIR

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
