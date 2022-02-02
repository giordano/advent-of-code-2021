#!/usr/bin/env python3

from os import path
import sys
import collections


def count_fishes(timers, days):
    timers_count = collections.Counter(timers)
    ages = range(0, 9)
    # Make sure all ages from 0 to 8 have a value
    for age in ages:
        timers_count[age] = timers_count.get(age, 0)

    for _ in range(1, days + 1):
        # Remember number of fishes with timer == 0
        zeros = timers_count[0]
        # Shift all timers
        for age in range(1, 9):
            timers_count[age - 1] = timers_count[age]
        # In addition to the fishes with timer == 7 that decreased, for timer
        # == 6 now there are also the fishes that had timer == 0.
        timers_count[6] += zeros
        # All fishes that initially had timer == 0 generated a brand-new fish
        # with timer == 8.
        timers_count[8] = zeros
    return sum(timers_count.values())

def part1(timers):
    n = 80
    print("Part 1:")
    print(f"    Number of fishes after {n} days: {count_fishes(timers, n)}")
    return


def part2(ages):
    n = 256
    print("Part 2:")
    print(f"    Number of fishes after {n} days: {count_fishes(ages, n)}")
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')


    with open(filename, "r") as file:
        timers = [int(t) for t in file.read().split(",")]

    part1(timers)
    part2(timers)
