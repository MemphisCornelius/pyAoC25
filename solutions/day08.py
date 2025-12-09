import time
import heapq

input: str = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

input: str = open("inputs/day08", "r").read()


def parseInput():
    boxes: list[tuple[int, int, int]] = []
    for line in input.split("\n"):
        if not line:
            continue
        c = line.split(",")
        boxes.append((int(c[0]), int(c[1]), int(c[2])))
    return boxes


def part1():
    start: float = time.time()
    boxes: list[tuple[int, int, int]] = parseInput()
    box_with_circuit: dict[tuple[int, int, int], int] = dict(
        zip(boxes, range(0, len(boxes)))
    )
    pairs: list[tuple[tuple[int, int, int], tuple[int, int, int]]] = [
        (x, y) for x in boxes for y in boxes if x != y
    ]

    pairs_cleand: set[tuple[tuple[int, int, int], tuple[int, int, int]]] = set()

    for x, y in pairs:
        if (y, x) in pairs_cleand:
            continue
        pairs_cleand.add((x, y))

    pairs_with_distance: list[
        tuple[float, tuple[tuple[int, int, int], tuple[int, int, int]]]
    ] = [(calcDistance(x, y), (x, y)) for (x, y) in pairs_cleand]

    heapq.heapify(pairs_with_distance)

    for i in range(1000):
        (_, (x, y)) = heapq.heappop(pairs_with_distance)

        circuit_x: int = box_with_circuit[x]
        circuit_y: int = box_with_circuit[y]
        if circuit_x == circuit_y:
            continue

        min_circuit: int = min(circuit_x, circuit_y)
        max_circuit: int = max(circuit_x, circuit_y)

        for box in box_with_circuit:
            if box_with_circuit[box] == max_circuit:
                box_with_circuit[box] = min_circuit

    circuit_sizes: dict[int, int] = {}

    for box in box_with_circuit:
        if box_with_circuit[box] not in circuit_sizes:
            circuit_sizes[box_with_circuit[box]] = 1
        else:
            circuit_sizes[box_with_circuit[box]] += 1

    sorted_circuit_sizes: list[int] = list(
        dict(sorted(circuit_sizes.items(), key=lambda item: item[1])).values()
    )[::-1]
    sum: int = 1
    for i in range(0, 3):
        sum *= sorted_circuit_sizes[i]

    end: float = time.time()

    return (sum, end - start)


def calcDistance(x: tuple[int, int, int], y: tuple[int, int, int]):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2


def part2():
    start: float = time.time()
    boxes: list[tuple[int, int, int]] = parseInput()
    box_with_circuit: dict[tuple[int, int, int], int] = dict(
        zip(boxes, range(0, len(boxes)))
    )
    pairs: list[tuple[tuple[int, int, int], tuple[int, int, int]]] = [
        (x, y) for x in boxes for y in boxes if x != y
    ]

    pairs_cleand: set[tuple[tuple[int, int, int], tuple[int, int, int]]] = set()

    for x, y in pairs:
        if (y, x) in pairs_cleand:
            continue
        pairs_cleand.add((x, y))

    pairs_with_distance: list[
        tuple[float, tuple[tuple[int, int, int], tuple[int, int, int]]]
    ] = [(calcDistance(x, y), (x, y)) for (x, y) in pairs_cleand]

    heapq.heapify(pairs_with_distance)

    while True:
        (_, (x, y)) = heapq.heappop(pairs_with_distance)

        circuit_x: int = box_with_circuit[x]
        circuit_y: int = box_with_circuit[y]
        if circuit_x == circuit_y:
            continue

        for box in box_with_circuit:
            if box_with_circuit[box] == max(circuit_x, circuit_y):
                box_with_circuit[box] = min(circuit_x, circuit_y)

        if all_in_same_circuit(box_with_circuit):
            ans: int = x[0] * y[0]
            end: float = time.time()
            return (ans, end - start)

    end = time.time()
    return (_, end - start)


def all_in_same_circuit(bc: dict[tuple[int, int, int], int]):
    first_circuit: int = bc[list(bc)[0]]
    for b in bc:
        if bc[b] != first_circuit:
            return False
    return True


print("Part 1: ", part1())
print("Part 2: ", part2())
