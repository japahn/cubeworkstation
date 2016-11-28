from collections import defaultdict
import webbrowser

from booster_output import output_boosters
from the_cube import TheCube

class BoosterStats(object):

    def __init__(self, cube):
        self._section_names = sorted(cube.sections().keys())
        self._boosters_seen = 0
        self._section_distribution = defaultdict(lambda: defaultdict(int))

    def process_booster(self, booster):
        self._boosters_seen += 1
        cards_per_section = defaultdict(int)
        for card in booster.cards():
            cards_per_section[card.section()] += 1

        for section_name in self._section_names:
            cards_in_section = cards_per_section[section_name]
            self._section_distribution[section_name][cards_in_section] += 1

    def output(self):
        print 'Booster Stats for %d boosters' % self._boosters_seen
        print
        for section_name in self._section_names:
            num_distributions = len(self._section_distribution[section_name])
            if num_distributions == 0:
                continue

            if (num_distributions == 1
                and (0 in self._section_distribution[section_name].keys())):
                continue

            print 'Section %s:' % section_name
            max_occurrences = max(self._section_distribution[section_name].keys())
            for num_occurrences in xrange(max_occurrences + 1):
                frequency = self._section_distribution[section_name][num_occurrences]
                percentage = float(frequency) / self._boosters_seen
                print '    %d occurrences: %d (%s)'\
                      % (num_occurrences, frequency, '{:.2%}'.format(percentage))
            print

RUNS = 1
OUTPUT_TO_HTML = True

if __name__ == '__main__':
    the_cube = TheCube()

    booster_stats = BoosterStats(the_cube.cube())

    for r in xrange(RUNS):
        boosters = the_cube.good_stuff_draft(8)
        # boosters = the_cube.full_random_draft(8)

        for b in boosters:
            b.sort_by_section()
            booster_stats.process_booster(b)

    if OUTPUT_TO_HTML:
        output_boosters('output/boosters.html', boosters)
        webbrowser.open('output/boosters.html')

    booster_stats.output()
