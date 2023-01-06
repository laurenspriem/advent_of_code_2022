# load data
with open("../input/day02_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("../input/day02_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()

import numpy as np

# transform input example
challenge_input_sample = challenge_input_sample.split("\n")
challenge_input_sample = [
    [strategy[0], strategy[2]] for strategy in challenge_input_sample
]

# transform input
challenge_input = challenge_input.split("\n")
challenge_input = [[strategy[0], strategy[2]] for strategy in challenge_input]


def calculate_score(challenge_input_variable):
    """
    input: list of all rounds, containing for each round (row) first opponents strategy and then my strategy (Rock,Paper Scissor = A,B,C or X,Y,Z)
    output: score depending on win and on chosen own strategy
    """
    input_np = np.array(challenge_input_variable)
    # strategy score
    strategy_score = (
        sum(input_np[:, 1] == "X")
        + 2 * sum(input_np[:, 1] == "Y")
        + 3 * sum(input_np[:, 1] == "Z")
    )
    # win score
    win_score = 0
    for round in challenge_input_variable:
        if round == ["A", "X"]:
            win_score += 3
        elif round == ["B", "Y"]:
            win_score += 3
        elif round == ["C", "Z"]:
            win_score += 3
        elif round == ["A", "Z"]:
            win_score += 0
        elif round == ["B", "X"]:
            win_score += 0
        elif round == ["C", "Y"]:
            win_score += 0
        elif round == ["A", "Y"]:
            win_score += 6
        elif round == ["B", "Z"]:
            win_score += 6
        elif round == ["C", "X"]:
            win_score += 6

    return strategy_score + win_score


print(f"Answer: {calculate_score(challenge_input)}")


def calculate_score_V2(challenge_input_variable):
    """
    input: list of all rounds, containing for each round (row) first opponents strategy and then my strategy (Rock,Paper Scissor = A,B,C or X,Y,Z)
    output: score depending on win and on chosen own strategy, now given the fact that X,Y,X decides whether you win or lose
    """
    input_np = np.array(challenge_input_variable)
    # win score
    win_score = (
        0 * sum(input_np[:, 1] == "X")
        + 3 * sum(input_np[:, 1] == "Y")
        + 6 * sum(input_np[:, 1] == "Z")
    )
    # strategy score
    strategy_score = 0
    for round in challenge_input_variable:
        if round == ["A", "X"]:
            strategy_score += 3
        elif round == ["B", "Y"]:
            strategy_score += 2
        elif round == ["C", "Z"]:
            strategy_score += 1
        elif round == ["A", "Z"]:
            strategy_score += 2
        elif round == ["B", "X"]:
            strategy_score += 1
        elif round == ["C", "Y"]:
            strategy_score += 3
        elif round == ["A", "Y"]:
            strategy_score += 1
        elif round == ["B", "Z"]:
            strategy_score += 3
        elif round == ["C", "X"]:
            strategy_score += 2

    return strategy_score + win_score


print(f"Answer: {calculate_score_V2(challenge_input)}")
