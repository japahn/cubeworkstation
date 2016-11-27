from card import Card
from card_pile import CardPile

def read_text_pool(file_name):
    with file(file_name) as f:
        lines = f.readlines()
    lines = map(lambda s: s.strip(), lines)
    cards = map(lambda s: Card(s), lines)
    card_pile = CardPile(file_name, cards)
    return card_pile

def read_all_mods():
    mod_lands_pile = read_text_pool('data/mod_lands.txt')
    print mod_lands_pile

if __name__ == '__main__':
    read_all_mods()
