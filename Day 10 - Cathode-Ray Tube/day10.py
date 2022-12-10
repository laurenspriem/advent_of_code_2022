# load data
with open("Day 10 - Cathode-Ray Tube/input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("Day 10 - Cathode-Ray Tube/input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def part1(challenge_input_variable):
    x = 1
    cycles = [x]
    for line in challenge_input_variable.splitlines():
        match line.split():
            case ["addx", number]:
                cycles.append(x)
                cycles.append(x)
                x += int(number)
            case ["noop"]:
                cycles.append(x)
    return sum([cycle * x for cycle, x in list(enumerate(cycles))[20::40]])


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input_variable):
    x = 1
    cycles = [x]
    for line in challenge_input_variable.splitlines():
        match line.split():
            case ["addx", number]:
                cycles.append(x)
                cycles.append(x)
                x += int(number)
            case ["noop"]:
                cycles.append(x)
    for row in range(0, len(cycles) - 1, 40):
        for pixel in range(40):
            if abs(cycles[row + pixel + 1] - pixel) <= 1:
                print(end="#")
            else:
                print(end=" ")
        print()


print("Answer:")
part2(challenge_input)
