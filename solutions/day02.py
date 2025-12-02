import time

input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = open("inputs/day02", "r").read()


def part1():
    start = time.time()
    sum: int = 0

    for pair in input.split(","):
        interval = pair.split("-")
        for id in range(int(interval[0]), int(interval[1]) + 1):
            str_id: str = str(id)
            if len(str_id) % 2 == 0:
                half: int = int(len(str_id) / 2)
                if str_id[:half] == str_id[half:]:
                    sum += id
    end = time.time()
    return (sum, end - start)


def part2():
    start = time.time()
    sum: int = 0

    for pair in input.split(","):
        interval = pair.split("-")
        for id in range(int(interval[0]), int(interval[1]) + 1):
            str_id: str = str(id)
            if hasReapeatingdigis(str_id):
                sum += id
    end = time.time()
    return (sum, end - start)


def hasReapeatingdigis(s: str):
    for n in range(1, len(s)):
        if len(s) % n != 0:
            continue
        splits = [s[i : i + n] for i in range(0, len(s), n)]
        equal = True
        for split in splits:
            if split != splits[0]:
                equal = False
                break
        if equal:
            return True
    return False


print("part1: ", part1())
print("part2: ", part2())
