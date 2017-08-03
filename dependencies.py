#!/usr/bin/env python

import sys


def readfile(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    return lines

def find_depend_indcs(lines):
    n_lines = len(lines)
    indcs = []
    persist = True
    i = 0
    while (i < n_lines) and persist:
        if lines[i] == 'requirements:':
            for l in range(i, n_lines):
                if lines[l] == 'test:':
                    persist = False
                    break
                elif lines[l][0:8] == '    - r-':
                    indcs.append(l)
        i += 1
    return indcs


def package_name(pkg_string):
    res = pkg_string.split(' ')[0]
    return res


def _find_dependencies(lines, indcs):
    depends = [lines[i][8:] for i in indcs]
    res = []
    for pkg in depends:
        if pkg != 'base':
            res.append(package_name(pkg))
    return list(set(res))

def find_dependencies(filename):
    lines = readfile(filename)
    indcs = find_depend_indcs(lines)
    res = _dependencies(lines, indcs)
    return res
