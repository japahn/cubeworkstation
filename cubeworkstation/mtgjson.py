import json

SECTION_W = '1. W'
SECTION_U = '2. U'
SECTION_B = '3. B'
SECTION_R = '4. R'
SECTION_G = '5. G'
SECTION_OTHER = '6. Other'
ALL_SECTIONS = [
    SECTION_W,
    SECTION_U,
    SECTION_B,
    SECTION_R,
    SECTION_G,
    SECTION_OTHER,
]

_OVERRIDES = {
    # Opponent action
    'Quenchable Fire': SECTION_R,

    # Multicolored by optional ability
    'Soulfire Grand Master': SECTION_W,
    'Brutal Hordechief': SECTION_B,
    'Alesha, Who Smiles at Death': SECTION_R,
    'Warden of the First Tree': SECTION_G,
    'Yasova Dragonclaw': SECTION_G,

    # De facto multicolored due to text
    'Kird Ape': SECTION_OTHER,

    # Artifacts with activation costs
    'Scrapheap Scrounger': SECTION_OTHER,
    'Cranial Plating': SECTION_OTHER,
}

_SECTION_PER_IDENTITY = {
    'W': SECTION_W,
    'U': SECTION_U,
    'B': SECTION_B,
    'R': SECTION_R,
    'G': SECTION_G,
}

class CardDatabase(object):

    def __init__(self):
        self._db = None

    def set_database(self, db):
        self._db = db

    def get(self):
        return self._db


_SPLIT_CARD_SEPARATOR = ' // '

ALL_CARDS = CardDatabase()


def build_database():
    with file('cubeworkstation/data/AllCards.json') as f:
        ALL_CARDS.set_database(json.load(f))

def get_section(card_name):
    override = _OVERRIDES.get(card_name)
    if override is not None:
        return override

    if _SPLIT_CARD_SEPARATOR in card_name:
        card_name1, card_name2 = card_name.split(_SPLIT_CARD_SEPARATOR)
        section1, section2 = get_section(card_name1), get_section(card_name2)
        if section1 == section2:
            return section1
        else:
            return SECTION_OTHER

    card_info = ALL_CARDS.get()[card_name]

    supertypes_and_types = get_supertypes_and_types(card_info)
    if 'Land' in supertypes_and_types:
        return SECTION_OTHER

    color_identity = card_info.get('colorIdentity')
    return get_section_for_identity(color_identity)

def get_section_for_identity(identity):
    if identity is None or len(identity) != 1:
        return SECTION_OTHER
    else:
        return _SECTION_PER_IDENTITY[identity[0]]

def get_supertypes_and_types(card_info):
    type_line = card_info['type']
    # u"\u2014" is the long dash
    return type_line.split(u"\u2014")[0].strip().split(' ')

build_database()

if __name__ == '__main__':
    # Mono color simple
    assert get_section('Counterspell') == SECTION_U

    # Multi by cost
    assert get_section('Blightning') == SECTION_OTHER

    # Multi by hybrid
    assert get_section('Rakdos Cackler') == SECTION_OTHER

    # Multi by identity
    assert get_section('Jilt') == SECTION_OTHER

    # Artifact
    assert get_section('Sol Ring') == SECTION_OTHER

    # Colored artifact
    assert get_section('Birthing Pod') == SECTION_G

    # Override
    assert get_section('Quenchable Fire') == SECTION_R

    # De facto colored artifact
    assert get_section('Shrine of Burning Rage') == SECTION_OTHER

    # Land
    assert get_section('Treetop Village') == SECTION_OTHER

    # Legendary "Colored" Land
    assert get_section('Karakas') == SECTION_OTHER

    # Legendary Snow Land
    assert get_section('Dark Depths') == SECTION_OTHER

    # Mono-color split card
    assert get_section('Dead // Gone') == SECTION_R

    # Multicolor split card
    assert get_section('Life // Death') == SECTION_OTHER

    print 'OK'
