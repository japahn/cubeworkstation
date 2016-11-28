from booster_output import output_boosters
from the_cube import TheCube


if __name__ == '__main__':
    cube = TheCube()

    boosters = cube.good_stuff_draft(8)

    output_boosters('output/boosters.html', boosters)
