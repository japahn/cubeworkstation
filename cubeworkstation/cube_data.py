import os

from card import Card
from cube_module import CubeModule

DATA_DIR = 'cubeworkstation/data/card_modules'

def read_text_pool(module_name, file_name):
    with file('%s/%s' % (DATA_DIR, file_name)) as f:
        lines = f.readlines()
    lines = map(lambda s: s.strip(), lines)
    cards = map(lambda s: Card(s), lines)

    return CubeModule(module_name, cards)


MODULES = {}

def _read_modules():
    for module_file_name in os.listdir(DATA_DIR):
        module_name = module_file_name.split('.')[0]
        pools = read_text_pool(module_name, module_file_name)
        MODULES[module_name] = pools

_read_modules()
