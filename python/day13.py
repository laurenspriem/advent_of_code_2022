# load data
with open("input/day13_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("input/day13_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def comparison(left, right):
    if type(left) == type(right) == int:
        if left - right < 0:
            return True  # "correct"
        elif left - right > 0:
            return False  # "incorrect"
        else:
            return "equal"
    elif type(left) == int and type(right) != int:
        return comparison([left], right)
    elif type(left) != int and type(right) == int:
        return comparison(left, [right])

    for left_element, right_element in zip(left, right):
        test = comparison(left_element, right_element)
        if test == True:
            return True
        elif test == False:
            return False

    if len(left) - len(right) < 0:
        return True
    elif len(left) - len(right) > 0:
        return False


def part1(challenge_input):
    pairs = [list(pair.splitlines()) for pair in challenge_input.strip().split("\n\n")]
    points = 0
    for idx, (left, right) in enumerate(pairs):
        if comparison(eval(left), eval(right)):
            points += idx + 1

    return points


print(f"Answer: {part1(challenge_input_sample)}")


def part2(challenge_input):
    packets = [line for line in challenge_input.strip().split()]
    idx_2, idx_6 = 1, 2
    for packet in packets:
        if comparison(eval(packet), [[2]]):
            idx_2 += 1
            idx_6 += 1
        elif comparison(eval(packet), [[6]]):
            idx_6 += 1

    return idx_2 * idx_6


print(f"Answer: {part2(challenge_input)}")
