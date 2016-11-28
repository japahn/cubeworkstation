import webbrowser

from booster_output import output_boosters
from booster_stats import BoosterStats
from the_cube import TheCube

RUNS = 1
OUTPUT_TO_HTML = True
HTML_LOCATION ='output/boosters.html'

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
        output_boosters(HTML_LOCATION, boosters)
        webbrowser.open(HTML_LOCATION)

    booster_stats.output()
