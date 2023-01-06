# load data
with open("../input/day03_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read().split("\n")
with open("../input/day03_input.txt", encoding="utf-8") as f:
    challenge_input = f.read().split("\n")

from string import ascii_letters


def Sum_priorities(challenge_input_variable):
    """Returns the sum of the priorities of the common items in the elves rucksacks"""
    rucksacks = []
    common_characters = []
    points = 0
    scores = {key: value for (key, value) in zip(ascii_letters, range(1, 53))}
    for string in challenge_input_variable:
        length = int(len(string) / 2)
        compartment1 = set(string[0:length])
        compartment2 = set(string[length:])
        rucksacks.append((compartment1, compartment2))
        test = compartment1.intersection(compartment2)
        common_character = "".join(compartment1.intersection(compartment2))
        common_characters.append(common_character)
        points += scores[common_character]

    return points


print(f"Answer: {Sum_priorities(challenge_input)}")


def Sum_badges(challenge_input_variable):
    """Returns the sum of the priorities of each badge group"""
    items = []
    badges = []
    points = 0
    scores = {key: value for (key, value) in zip(ascii_letters, range(1, 53))}
    for string, counter in zip(
        challenge_input_variable, range(1, len(challenge_input_variable) + 1)
    ):

        items.append(set(string))
        if counter % 3 == 0:
            badge = "".join(set.intersection(items[-1], items[-2], items[-3]))
            badges.append(badge)
            points += scores[badge]

    return points


print(f"Answer: {Sum_badges(challenge_input)}")
