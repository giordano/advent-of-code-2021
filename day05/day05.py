#!/usr/bin/env python3

from os import path
import sys


class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # To pretty print the class
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    # Define equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Make the class hashable, to be used in a dictionary
    def __hash__(self):
        return hash((self.x, self.y))


class LineSegment():
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    # To pretty print the class
    def __repr__(self):
        return f"{self.p1} -> {self.p2}"

    def is_horizontal(self):
        return self.p1.x == self.p2.x

    def is_vertical(self):
        return self.p1.y == self.p2.y

    def covered_points(self, diagonal):
        if self.is_horizontal():
            return [
                Point(self.p1.x, y)
                for y in range(min(self.p1.y, self.p2.y),
                               max(self.p1.y, self.p2.y) + 1)
            ]
        elif self.is_vertical():
            return [
                Point(x, self.p1.y)
                for x in range(min(self.p1.x, self.p2.x),
                               max(self.p1.x, self.p2.x) + 1)
            ]
        else:
            if diagonal:
                # TODO: implement diagonal line segments.
                return []
            else:
                return []


def part1(data):

    points = []
    for line_segment in data:
        points += line_segment.covered_points(diagonal=False)
    freqs = dict((x, points.count(x)) for x in set(points))

    print("Part 1:")
    print(f"    overlapping points: {sum(x > 1 for x in freqs.values())}")
    return


def part2(data):

    points = []
    for line_segment in data:
        points += line_segment.covered_points(diagonal=True)
    freqs = dict((x, points.count(x)) for x in set(points))

    print("Part 2:")
    print(f"    overlapping points: {sum(x > 1 for x in freqs.values())}")
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')

    # Open the file in binary mode, read-only
    file = open(filename, "r")

    # Parse the file as a bit matrix
    data = []
    for line in file:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        data.append(LineSegment(int(x1), int(y1), int(x2), int(y2)))

    file.close()

    part1(data)
    part2(data)
