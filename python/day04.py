# load data
with open("../input/day04_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read().split("\n")
with open("../input/day04_input.txt", encoding="utf-8") as f:
    challenge_input = f.read().split("\n")


def part1(challenge_input_variable):
    points = 0
    for pairs in challenge_input_variable:
        temp = [int(number) for elf in pairs.split(",") for number in elf.split("-")]
        assignments = [
            {s for s in range(temp[0], temp[1] + 1)},
            {s for s in range(temp[2], temp[3] + 1)},
        ]
        if assignments[0].issubset(assignments[1]):
            points += 1
        elif assignments[1].issubset(assignments[0]):
            points += 1

    return points


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input_variable):
    points = 0
    for pairs in challenge_input_variable:
        temp = [int(number) for elf in pairs.split(",") for number in elf.split("-")]
        assignments = [
            {s for s in range(temp[0], temp[1] + 1)},
            {s for s in range(temp[2], temp[3] + 1)},
        ]
        if bool(assignments[0] & assignments[1]):
            points += 1

    return points


print(f"Answer: {part2(challenge_input)}")
