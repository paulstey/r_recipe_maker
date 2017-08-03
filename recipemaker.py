#!/usr/bin/env python

import os
import sys
from subprocess import call

def get_package_name():
    res = sys.argv[1]
    return res


def write_recipe(pkg):
    call(['conda', 'skeleton', 'cran', pkg])


def recipe_exists(pkg):
    dirname = 'r-' + pkg
    res = os.path.isdir(dirname)
    return res


def main():
    pkg = get_package_name()
    if recipe_exists(pkg):
        print("The recipe for", pkg, "already exists...")
    else:
        print("Writing recipe for:", pkg)
        write_recipe(pkg)

if __name__ == '__main__':
    main()
