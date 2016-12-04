#!/usr/bin/env python

import os

from cubeworkstation.cube_data import DATA_DIR


def main():
    for file_name in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file_name)
        os.system('sort %s -o %s' % (file_path, file_path))

if __name__ == '__main__':
    main()
