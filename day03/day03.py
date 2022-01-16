#!/usr/bin/env python3

from os import path
import sys
import numpy as np

def get_rate(bits):
    return sum(b * 2 ** n for (n, b) in enumerate(reversed(bits)))

def part1(bm):
    n_rows, n_cols = bm.shape
    gamma_bit = sum(bm) > (n_rows / 2)
    gamma_rate = get_rate(gamma_bit)
    # No need to recompute the epsilon rate: it's the complementary of
    # `gamma_rate` to 2 ** n_cols - 1
    epsilon_rate = 2 ** n_cols - 1 - gamma_rate

    print("Part 1:")
    print(f"    Gamma rate:        {gamma_rate}")
    print(f"    Epsilon rate:      {epsilon_rate}")
    print(f"    Power consumption: {gamma_rate * epsilon_rate}")
    return


def get_rating(bit_matrix, bit):
    n_rows, n_cols = bit_matrix.shape
    mask = np.ones(n_rows, dtype=bool)
    for col in range(0, n_cols):
        # Get the sum of the bits in the current column
        tot = sum(bit_matrix[mask, col])
        if tot == sum(mask) / 2:
            # If it's equal to half the number of rows left (== the total of
            # `True` elements of the `mask`), then use the favourite `bit`.
            this_bit = bit
        else:
            # If `bit` is 1, then use the most common bit, othwerise use the
            # least common bit.  TODO: the logic most/least common shouldn't be
            # tied to the value of the favourite bit.
            if bit:
                this_bit = tot > (sum(mask) / 2)
            else:
                this_bit = tot < (sum(mask) / 2)
        # Keep only the rows equal to the current bit.  TODO: this can probably
        # be optimised by comparing only the active rows.
        mask &= bit_matrix[:, col] == this_bit

        # If there is only one number left, leave early
        if sum(mask) <= 1:
            break

    return get_rate(bit_matrix[mask][0])


def part2(bm):
    oxygen_rating = get_rating(bm, 1)
    co2_rating = get_rating(bm, 0)

    print("Part 2:")
    print(f"    Oxygen generator rating: {oxygen_rating}")
    print(f"    CO2 scrubber rating:     {co2_rating}")
    print(f"    life support rating:     {oxygen_rating * co2_rating}")
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')

    # Open the file in binary mode, read-only
    file = open(filename, "rb")

    # Parse the file as a bit matrix
    bm = np.array([
        # Manually drop newlines by filtering out characters below '0'.
        [b - ord('0') for b in line if b >= ord('0')]
        for line in file])

    file.close()

    part1(bm)
    part2(bm)
