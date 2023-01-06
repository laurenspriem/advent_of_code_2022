# load data
with open("../input/day06_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("../input/day06_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def part1(challenge_input):
    characters_list = []
    for count, character in enumerate(challenge_input):
        characters_list.append(character)
        if count >= 3:
            if len(set(characters_list[-4:])) == 4:
                return count + 1


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input):
    characters_list = []
    for count, character in enumerate(challenge_input):
        characters_list.append(character)
        if count >= 13:
            if len(set(characters_list[-14:])) == 14:
                return count + 1


print(f"Answer: {part2(challenge_input)}")
