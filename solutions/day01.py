input: str = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")

input: str = open("inputs/day01", "r").read().splitlines()


def part1():
    dial: int = 50
    zeros: int = 0

    for rotation in input:
        dir: int = 1 if rotation[0] == "R" else -1
        dial += dir * int(rotation[1:])
        dial %= 100

        if dial == 0:
            zeros += 1

    return zeros


def part2():
    dial: int = 50
    zeros: int = 0

    for rotation in input:
        old_dial: int = dial
        dir: int = 1 if rotation[0] == "R" else -1

        dial += int(rotation[1:]) * dir
        zeros += dial // (dir * 100)
        dial %= 100

        if dir == -1:
            if old_dial == 0:
                zeros -= 1
            zeros += 1

    return zeros


print("part1: " + str(part1()))
print("part2: " + str(part2()))
