from collections import defaultdict
import os

from card import Card
from card_pool import CardPool
from cube import Cube
import mtgjson

DATA_DIR = 'cubeworkstation/data/card_modules'

def read_text_pool(module_name, file_name):
    card_pools = {}

    with file('%s/%s' % (DATA_DIR, file_name)) as f:
        lines = f.readlines()
    lines = map(lambda s: s.strip(), lines)
    cards = map(lambda s: Card(s), lines)
    cards_by_section = defaultdict(list)
    for card in cards:
        color = mtgjson.get_section(card.name())
        cards_by_section[color].append(card)

    for color, section_cards in cards_by_section.iteritems():
        section_id = (module_name, color)
        card_pool = CardPool(section_id, section_cards)
        card_pools[section_id] = card_pool
        for card in section_cards:
            card.set_section(section_id)

    return card_pools


MODULES = {}

def _read_modules():
    for module_file_name in os.listdir(DATA_DIR):
        module_name = module_file_name.split('.')[0]
        pools = read_text_pool(module_name, module_file_name)
        MODULES[module_name] = pools

_read_modules()
