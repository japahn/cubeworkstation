class Card(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '[[%s]]' % self.name
