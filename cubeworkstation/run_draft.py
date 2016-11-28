from booster_output import output_boosters
from the_cube import TheCube


if __name__ == '__main__':
    cube = TheCube()

    # boosters = cube.good_stuff_draft(8)
    boosters = cube.full_random_draft(8)

    for booster in boosters:
        booster.sort_by_section()

    output_boosters('output/boosters.html', boosters)
