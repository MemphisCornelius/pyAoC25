import time

input: str = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

input: str = open("inputs/day07", "r").read()


def part1():
    start: float = time.time()
    sum: int = 0

    diagram: list[str] = input.split("\n")
    for e in range(0, len(diagram)):
        if not diagram[e]:
            diagram.pop(e)

    start: int = diagram[0].index("S")
    diagram[1] = replace_at(diagram[1], start, "|")

    for i in range(1, len(diagram) - 1):
        for k in range(0, len(diagram[i])):
            if diagram[i][k] != "|":
                continue
            if diagram[i + 1][k] == "^":
                sum += 1
                diagram[i + 1] = replace_at(diagram[i + 1], k - 1, "|")
                diagram[i + 1] = replace_at(diagram[i + 1], k + 1, "|")
            else:
                diagram[i + 1] = replace_at(diagram[i + 1], k, "|")

    end: float = time.time()
    return (sum, end - start)


def replace_at(s: str, i: int, r: str):
    return s[:i] + r + s[i + 1 :]


print("Part 1: ", part1())
