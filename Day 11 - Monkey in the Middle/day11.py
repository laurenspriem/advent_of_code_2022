# load data
with open("Day 11 - Monkey in the Middle/input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("Day 11 - Monkey in the Middle/input.txt", encoding="utf-8") as f:
    challenge_input = f.read()

import re
from math import lcm


def monkey_dict(information):
    """Parse the monkey information to a monkey dict"""
    information = information.splitlines()
    monkey = {
        "items": list(map(int, re.findall("[0-9]+", information[1]))),
        "operation": lambda old: eval(
            re.search("\= (.*)", information[2])[0].replace("= ", "")
        ),
        "test": lambda x: x % int(re.search("[0-9]+", information[3])[0]) == 0,
        "divisor": int(re.search("[0-9]+", information[3])[0]),
        "iftrue": (int(re.search("[0-9]+", information[4])[0])),
        "iffalse": int(re.search("[0-9]+", information[5])[0]),
    }
    return monkey


def part1(challenge_input_variable):
    """return the level of monkey business after 20 rounds"""
    monkeys = [monkey_dict(info) for info in challenge_input_variable.split("\n\n")]
    active = [0] * len(monkeys)
    for dummy_round_nr in range(20):
        for idx, monkey in enumerate(monkeys):
            for _ in range(len(monkey["items"])):
                worry = monkey["items"].pop(0)
                active[idx] += 1
                worry = monkey["operation"](worry)
                worry //= 3
                throwto = (
                    monkey["iftrue"] if (monkey["test"](worry)) else monkey["iffalse"]
                )
                monkeys[throwto]["items"].append(worry)
    active_sorted = sorted(active)

    return active_sorted[-1] * active_sorted[-2]


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input_variable, number_of_rounds=10000):
    """return the level of monkey business after 10000 rounds"""
    monkeys = [monkey_dict(info) for info in challenge_input_variable.split("\n\n")]
    common_multiple = lcm(*(monkey["divisor"] for monkey in monkeys))
    active = [0] * len(monkeys)
    print(common_multiple)
    for dummy_round_nr in range(number_of_rounds):
        for idx, monkey in enumerate(monkeys):
            for _ in range(len(monkey["items"])):
                worry = monkey["items"].pop(0)
                active[idx] += 1
                worry = monkey["operation"](worry)
                worry %= common_multiple
                throwto = (
                    monkey["iftrue"] if (monkey["test"](worry)) else monkey["iffalse"]
                )
                monkeys[throwto]["items"].append(worry)
    active_sorted = sorted(active)

    return active_sorted[-1] * active_sorted[-2]


print(f"Answer: {part2(challenge_input)}")
