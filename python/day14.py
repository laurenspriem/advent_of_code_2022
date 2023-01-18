# load data
with open("input/day14_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read().strip()
with open("input/day14_input.txt", encoding="utf-8") as f:
    challenge_input = f.read().strip()


def parse_input(challenge_input):
    positions = set()
    ending = 0
    for line in challenge_input.splitlines():
        coordinates = [
            list(map(int, coordinate.split(","))) for coordinate in line.split(" -> ")
        ]
        for loc1, loc2 in zip(coordinates, coordinates[1:]):
            [x1, x2], [y1, y2] = sorted([loc1[0], loc2[0]]), sorted([loc1[1], loc2[1]])
            ending = max(ending, y2)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    positions.add(complex(x, y))

    return positions, ending


def part1(challenge_input):
    positions, ending = parse_input(challenge_input)
    start = complex(500, 0)
    points = 0

    try:
        while True:
            sand = start
            while True:
                if sand.imag >= ending:
                    raise Exception
                if sand + 1j not in positions:
                    sand += 1j
                    continue
                if sand - 1 + 1j not in positions:
                    sand += -1 + 1j
                    continue
                if sand + 1 + 1j not in positions:
                    sand += 1 + 1j
                    continue
                points += 1
                positions.add(sand)
                break
    except Exception:
        pass
    return points


print(f"Part1: {part1(challenge_input)}")


def part2(challenge_input):
    positions, ending = parse_input(challenge_input)
    start = complex(500, 0)
    points = 0

    while start not in positions:
        sand = start
        while True:
            if sand.imag >= ending + 1:
                points += 1
                positions.add(sand)
                break
            if sand + 1j not in positions:
                sand += 1j
                continue
            if sand - 1 + 1j not in positions:
                sand += -1 + 1j
                continue
            if sand + 1 + 1j not in positions:
                sand += 1 + 1j
                continue
            points += 1
            positions.add(sand)
            break
    return points


print(f"Part2: {part2(challenge_input)}")
