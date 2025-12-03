import time
input = """987654321111111
811111111111119
234234234234278
818181911112111""".split("\n")

input: list[str] = open("inputs/day03", "r").read().splitlines()


def part1():
    start = time.time()
    sum: int = 0
    for bank in input:
        pos1 = findlargestdigit(bank, 0, len(bank) - 1)
        pos2 = findlargestdigit(bank, pos1+1, len(bank))
        sum += int(bank[pos1]+bank[pos2])
    end = time.time()
    return (sum, end-start)


def part2():
    start = time.time()
    sum: int = 0
    for bank in input:
        pos: list[int] = []
        for i in range(0, 12):
            s = pos[i-1] + 1 if i > 0 else 0
            e = len(bank) - (11-i)
            pos.append(findlargestdigit(bank, s, e))
        sum += int("".join([bank[p] for p in pos]))
    end = time.time()
    return (sum, end-start)


def findlargestdigit(s: str, i: int, j: int):
    pos = i
    for p in range(i, j):
        if int(s[p]) > int(s[pos]):
            pos = p
    return pos


print("Part 1: ", part1())
print("Part 2: ", part2())
