#!/usr/bin/env python3

from os import path
import sys
import numpy as np


def part1(outputs):
    lens = np.array([len(o) for o in outputs])
    res = np.count_nonzero(np.isin(lens, [2, 3, 4, 7]))
    ## Alternative:
    # res = np.count_nonzero(np.fromiter(map(lambda o: len(o) in (2, 3, 4, 7),
    #                                        outputs), dtype=bool))

    print("Part 1:")
    print(f"    Number of 1s, 4s, 7s, or 8s: {res}")
    return


# def part2():
#     n = 256
#     print("Part 2:")
#     print(f"    Number of fishes after {n} days: {count_fishes(ages, n)}")
#     return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')


    patterns = []
    outputs  = []
    with open(filename, "r") as file:
        for line in file:
            p, o = line.split(" | ")
            patterns.append(p)
            for s in o.rstrip().split(" "):
                outputs.append(s)

    part1(outputs)
    # part2()
