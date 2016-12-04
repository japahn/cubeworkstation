import webbrowser

from booster_output import output_boosters
from booster_stats import BoosterStats
from the_cube import TheCube
from the_rare_cube import TheRareCube

RUNS = 1
OUTPUT_TO_HTML = True
HTML_LOCATION ='output/boosters.html'
# CUBE = TheCube()
CUBE = TheRareCube()

if __name__ == '__main__':
    the_cube = CUBE

    booster_stats = BoosterStats(the_cube.cube())

    for r in xrange(RUNS):
        boosters = the_cube.good_stuff_draft(8)
        # boosters = the_cube.full_random_draft(8)

        for b in boosters:
            booster_stats.process_booster(b)

    if OUTPUT_TO_HTML:
        output_boosters(HTML_LOCATION, boosters)
        webbrowser.open(HTML_LOCATION)

    booster_stats.output()
