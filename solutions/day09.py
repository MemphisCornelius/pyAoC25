import time
input: str = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

input: str = open("inputs/day09").read()


def parse_input():
    coordinates: list[tuple[int, int]] = []
    for line in input.split("\n"):
        if not line:
            continue
        c = line.split(",")
        coordinates.append((int(c[0]), int(c[1])))
    return coordinates


def part1():
    start: float = time.time()
    coordinates: list[tuple[int, int]] = parse_input()
    pairs: list[tuple[tuple[int, int], tuple[int, int]]] = [
        (x, y) for x in coordinates for y in coordinates]

    m: int = 0
    for pair in pairs:
        area = (abs(pair[0][0] - pair[1][0]) + 1) * \
            (abs(pair[0][1] - pair[1][1])+1)
        m = max(m, area)

    end: float = time.time()
    return (m, end-start)


print("Part 1: ", part1())
