import time

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


print("Part 1: ", part1())
