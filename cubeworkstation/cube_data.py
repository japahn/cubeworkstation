from card import Card
from card_pile import CardPile
from cube import Cube

def read_text_pool(section_name, file_name):
    with file(file_name) as f:
        lines = f.readlines()
    lines = map(lambda s: s.strip(), lines)
    cards = map(lambda s: Card(s), lines)
    card_pile = CardPile(section_name, cards)
    return card_pile

def build_cube():
    cube = Cube()
    cube.add_section(read_text_pool('mod_lands', 'data/mod_lands.txt'))
    cube.add_section(read_text_pool('mod_main', 'data/mod_main.txt'))
    cube.add_section(read_text_pool('mod_simple', 'data/mod_simple.txt'))
    cube.add_section(read_text_pool('module1', 'data/module1.txt'))
    cube.add_section(read_text_pool('module2', 'data/module2.txt'))
    cube.add_section(read_text_pool('module3', 'data/module3.txt'))
    cube.add_section(read_text_pool('module4', 'data/module4.txt'))
    return cube

if __name__ == '__main__':
    cube = build_cube()
    print cube
