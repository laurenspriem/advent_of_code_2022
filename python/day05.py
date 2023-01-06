# load data
with open("../input/day05_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read().split("\n\n")
with open("../input/day05_input.txt", encoding="utf-8") as f:
    challenge_input = f.read().split("\n\n")

import re  # re.findall
from collections import deque


def part1(challenge_input):
    starting_positions, instructions = challenge_input[0], challenge_input[1]
    stacks = []
    for idx in range(len(starting_positions.split("\n")[-1])):
        if idx % 4 == 0:
            stacks.append(deque())
    for line in starting_positions.split("\n")[:-1]:
        for stack, idx in enumerate(range(1, len(line), 4)):
            if line[idx] != " ":
                stacks[stack].appendleft(line[idx])
    for line in instructions.split("\n"):
        amount, from_position, to_position = map(int, re.findall("[0-9]+", line))
        for _ in range(amount):
            temp = stacks[from_position - 1].pop()
            stacks[to_position - 1].append(temp)
    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input):
    starting_positions, instructions = challenge_input[0], challenge_input[1]
    stacks = []
    for idx in range(len(starting_positions.split("\n")[-1])):
        if idx % 4 == 0:
            stacks.append(deque())
    for line in starting_positions.split("\n")[:-1]:
        for stack, idx in enumerate(range(1, len(line), 4)):
            if line[idx] != " ":
                stacks[stack].appendleft(line[idx])
    for line in instructions.split("\n"):
        amount, from_position, to_position = map(int, re.findall("[0-9]+", line))
        if amount > 1:
            temp = deque()
            for _ in range(amount):
                temp.append(stacks[from_position - 1].pop())
            for _ in range(amount):
                stacks[to_position - 1].append(temp.pop())
        elif amount == 1:
            temp = stacks[from_position - 1].pop()
            stacks[to_position - 1].append(temp)
    answer = ""
    for stack in stacks:
        answer += stack[-1]

    return answer


print(f"Answer: {part2(challenge_input)}")
