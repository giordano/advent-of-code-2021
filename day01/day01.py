#!/usr/bin/env python3

import os
from pathlib import Path
import sys
import numpy as np


def part1(data):
    count = np.sum(np.diff(data) > 0, axis=0)
    print(count)
    return


def part2(data, width=3):
    windows = np.array([np.sum(data[i:i+width])
                        for i in range(0, len(data)-width+1)])
    count = np.sum(np.diff(windows) > 0, axis=0)
    print(count)
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = os.path.join(Path(__file__).resolve().parent, 'input')

    data = np.loadtxt(filename)
    part1(data)
    part2(data)
