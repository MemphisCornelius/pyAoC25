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
            ranges.append(((int(r[0]), int(r[1])+1)))
        else:
            ids.append(int(line))

    return (ranges, ids)


def part1():
    sum: int = 0
    (ranges, ids) = splitinput()

    for i in ids:
        for r in ranges:
            if r[0] <= i <= r[1]:
                sum += 1
                break

    return sum


print("Part 1: ", part1())
