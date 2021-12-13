#!/usr/bin/env python3

from os import path
import sys


class SubmarineState:
    def update(self, command, n):
        if command == "forward":
            self.forward(int(n))
        elif command == "up":
            self.up(int(n))
        elif command == "down":
            self.down(int(n))
        else:
            raise Exception(f"Unknown command {command}")


class SubmarineStatePart1(SubmarineState):
    def __init__(self):
        self.depth = 0
        self.h_position = 0

    def forward(self, n):
        self.h_position += n

    def up(self, n):
        self.depth -= n

    def down(self, n):
        self.up(-n)


class SubmarineStatePart2(SubmarineState):
    def __init__(self):
        self.depth = 0
        self.h_position = 0
        self.aim = 0

    def forward(self, n):
        self.h_position += n
        self.depth += self.aim * n

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.up(-n)


def part1(filename):
    submarine = SubmarineStatePart1()
    with open(filename) as file:
        for line in file:
            command, n = line.split()
            submarine.update(command, n)

    print("Part 1:")
    print(f"    Horizontal position: {submarine.h_position}")
    print(f"    Depth:               {submarine.depth}")
    print(f"    Product:             {submarine.h_position * submarine.depth}")
    return


def part2(data):
    submarine = SubmarineStatePart2()
    with open(filename) as file:
        for line in file:
            command, n = line.split()
            submarine.update(command, n)

    print("Part 2:")
    print(f"    Horizontal position: {submarine.h_position}")
    print(f"    Depth:               {submarine.depth}")
    print(f"    Product:             {submarine.h_position * submarine.depth}")
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = path.join(path.dirname(__file__), 'input')

    part1(filename)
    part2(filename)
