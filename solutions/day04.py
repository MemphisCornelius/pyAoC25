import time

input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split("\n")

input = open("inputs/day04").readlines()

matrix: list[list[str]] = [list(line) for line in input]


def part1():
    start = time.time()
    sum = 0

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if matrix[y][x] == "@" and numadjacent(x, y) < 4:
                sum += 1

    end = time.time()
    return (sum, end-start)


def part2():
    start = time.time()
    sum = 0

    while True:
        remove: list[tuple[int, int]] = []
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if matrix[y][x] == "@" and numadjacent(x, y) < 4:
                    sum += 1
                    remove.append((x, y))
        if not remove:
            break
        for (x, y) in remove:
            matrix[y][x] = "."

    end = time.time()
    return (sum, end-start)


def numadjacent(x: int, y: int):
    sum: int = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i < 0 or i >= len(matrix):
                continue
            if j < 0 or j >= len(matrix[i]):
                continue
            if i == y and j == x:
                continue
            if matrix[i][j] == "@":
                sum += 1

    return sum


print("part 1: ", part1())
print("part 2: ", part2())
