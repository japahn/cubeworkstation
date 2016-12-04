class Cube(object):
    def __init__(self):
        self._modules = {}
        self._sections = {}
        self._card_count = 0

    def modules(self):
        return self._modules

    def sections(self):
        return self._sections

    def add_module(self, module):
        self._modules[module.name()] = module
        for section in module.all_sections():
            self._add_section(section)

    def _add_section(self, pool):
        self._sections[pool.name()] = pool
        self._card_count += pool.size()

    def __str__(self):
        section_names = sorted(self._sections.keys())
        string_repr = '-- Cube (%d cards) --\n' % self._card_count
        for section_name in section_names:
            section = self._sections[section_name]
            string_repr += '%s (%d cards)\n' % (section.name(), section.size())
        string_repr += '-- end --'
        return string_repr
