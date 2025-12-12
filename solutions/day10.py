import time
input: str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

input: str = open("inputs/day10", "r").read()


def parse_input():
    instructions: list[tuple[str, list[frozenset[int]], list[int]]] = []

    for line in input.split("\n"):
        if not line:
            continue
        components: list[str] = line.split()
        lights: str = components[0][1:-1]
        buttons: list[frozenset[int]] = []
        joltages: list[int] = []

        for b in components[1:-1]:
            b = b[1:-1]
            bs: list[int] = []
            for i in b.split(","):
                bs.append(int(i))
            buttons.append(frozenset(bs))

        components[-1] = components[-1][1:-1]
        for j in components[-1].split(","):
            joltages.append(int(j))

        instructions.append((lights, buttons, joltages))
    return instructions


def part1():
    start: float = time.time()
    sum: int = 0

    for instrucion in parse_input():
        sum += solve_instruction(instrucion)

    end: float = time.time()
    return (sum, end-start)


def press_button(state: str, buttons: frozenset[int]):
    for button in buttons:
        new_light: str = "."
        if state[button] == ".":
            new_light = "#"
        state = state[0: button] + new_light + state[button+1:]
    return state


def solve_instruction(instrucion: tuple[str, list[frozenset[int]], list[int]]):
    instructions_to_try: dict[tuple[str, frozenset[int]], int] = {}
    for buttons in instrucion[1]:
        instructions_to_try[("." * (len(instrucion[0])), buttons)] = 0

    while True:
        instructions: list[tuple[str, frozenset[int]]] = list(
            instructions_to_try.keys())

        for instr in instructions:
            iteration: int = instructions_to_try[instr]
            new_state: str = press_button(instr[0], instr[1])
            if new_state == instrucion[0]:
                return iteration + 1

            for buttons in instrucion[1]:
                new_instruction: tuple[str, frozenset[int]] = (
                    new_state, buttons)
                if new_instruction not in instructions_to_try:
                    instructions_to_try[new_instruction] = iteration + 1
            _ = instructions_to_try.pop(instr)


print("Part 1: ", part1())
