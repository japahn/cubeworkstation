class Cube(object):
    def __init__(self):
        self._sections = {}
        self._section_order = []
        self._card_count = 0

    def sections(self):
        return self._sections

    def add_section(self, pile):
        self._sections[pile.name()] = pile
        self._section_order.append(pile.name())
        self._card_count += pile.size()

    def __str__(self):
        string_repr = '-- Cube (%d) --\n' % self._card_count
        for section_name in self._section_order:
            section = self.sections()[section_name]
            string_repr += '%s (%d)\n' % (section.name(), section.size())
        string_repr += '-- end --'
        return string_repr
