#!/usr/bin/env python3

from os import path
import sys
import numpy as np

def part1(filename):
    # Open the file in binary mode, read-only
    file = open(filename, "rb")

    # Parse the file as a bit matrix
    bm = np.array([
        # Manually drop newlines by filtering out characters below '0'.
        [b - ord('0') for b in line if b >= ord('0')]
        for line in file])

    file.close()

    n_rows, n_cols = bm.shape
    gamma_bit = sum(bm) > (n_rows // 2)
    gamma_rate = sum(b * 2 ** n for (n, b) in enumerate(reversed(gamma_bit)))
    # No need to recompute the epsilon rate: it's the complementary of
    # `gamma_rate` to 2 ** n_cols - 1
    epsilon_rate = 2 ** n_cols - 1 - gamma_rate

    print("Part 1:")
    print(f"    gamma_rate:        {gamma_rate}")
    print(f"    epilon_rate:       {epsilon_rate}")
    print(f"    Power consumption: {gamma_rate * epsilon_rate}")
    return


# def part2(data):
#     with open(filename) as file:
#         for line in file:

#     print("Part 2:")
#     print(f"    Horizontal position: {submarine.h_position}")
#     print(f"    Depth:               {submarine.depth}")
#     print(f"    Product:             {submarine.h_position * submarine.depth}")
#     return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')

    part1(filename)
    # part2(filename)
