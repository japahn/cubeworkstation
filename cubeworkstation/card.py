class Card(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return '[[%s]]' % self._name

    def name(self):
        return self._name