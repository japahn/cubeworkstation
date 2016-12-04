class Card(object):
    def __init__(self, name):
        self._name = name
        self._sections = set()

    def __str__(self):
        return '[[%s]]' % self._name

    def name(self):
        return self._name

    def sections(self):
        return self._sections

    def set_section(self, section):
        self._sections.add(section)
