import time
from functools import reduce

input: str = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

input: str = open("inputs/day06", "r").read()


def part1():
    start: float = time.time()
    sum: int = 0
    roll: list[list[str]] = []

    for line in input.split("\n"):
        elements: list[str] = line.split()
        for i in range(0, len(elements)):
            try:
                roll[i].append(elements[i])
            except IndexError:
                roll.append([elements[i]])

    for line in roll:
        operator: str = line[-1]
        lsum: int = 0 if operator == "+" else 1

        if operator == "+":
            for element in range(0, len(line) - 1):
                lsum += int(line[element])
        else:
            for element in range(0, len(line) - 1):
                lsum *= int(line[element])
        sum += lsum

    end: float = time.time()
    return (sum, end - start)


def part2():
    start: float = time.time()

    sum: int = 0
    lines: list[str] = input.split("\n")

    for e in range(0, len(lines)):
        if not lines[e]:
            lines.pop(e)

    nums: list[int] = []
    for i in range(len(lines[0]) - 1, -1, -1):
        num: str = ""
        for line in range(0, len(lines)):
            num += lines[line][i]
        num = num.strip()
        if not num:
            continue
        if "+" in num or "*" in num:
            operator: str = num[-1]
            num = num[:-1]
            nums.append(int(num))
            sum += calculate_row(operator, nums)
            nums = []
        else:
            nums.append(int(num))
    end: float = time.time()
    return (sum, end - start)


def calculate_row(operator: str, nums: list[int]):
    if operator == "+":
        return reduce(lambda x, y: x + y, nums)
    else:
        return reduce(lambda x, y: x * y, nums)


print("Part 1: ", part1())
print("Part 2: ", part2())
