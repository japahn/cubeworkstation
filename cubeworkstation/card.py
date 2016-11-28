class Card(object):
    def __init__(self, name):
        self._name = name
        self._section = None

    def __str__(self):
        return '[[%s]]' % self._name

    def name(self):
        return self._name

    def section(self):
        return self._section

    def set_section(self, section):
        self._section = section
