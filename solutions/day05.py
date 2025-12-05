import time

input: str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

input: str = open("inputs/day05", "r").read()


def splitinput():
    lines: list[str] = input.split("\n")
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []
    delim: bool = False

    for line in lines:
        if line == "":
            delim = True
            continue

        if not delim:
            r = line.split("-")
            ranges.append(((int(r[0]), int(r[1]))))
        else:
            ids.append(int(line))

    return (ranges, ids)


def part1():
    start = time.time()
    sum: int = 0
    (ranges, ids) = splitinput()

    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                sum += 1
                break
    end = time.time()
    return (sum, end-start)


def part2():
    start = time.time()
    sum: int = 0
    (ranges, _) = splitinput()

    ranges.sort()

    left: int = 0
    right: int = 0

    for i in range(1, len(ranges)):
        if ranges[left][0] < ranges[i][0] and ranges[right][1] > ranges[i][1]:
            continue

        if ranges[i][0] > ranges[right][1]:
            sum += (ranges[right][1] - ranges[left][0]) + 1
            left = i
            right = i
        else:
            right = i

    sum += (ranges[right][1] - ranges[left][0]) + 1
    end = time.time()
    return (sum, end - start)


print("Part 1: ", part1())
print("Part 2: ", part2())
