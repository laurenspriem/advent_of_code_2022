# load data
with open("../input/day01_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("../input/day01_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def Max_Calories_Elves(challenge_input_variable):
    """
    input: string with \n and \n\n
    output: max calories and index of elve
    """
    input_example_elves = challenge_input_variable.split("\n\n")
    calorie_list = [
        sum(list(map(int, number.split("\n")))) for number in input_example_elves
    ]
    max_calorie = max(calorie_list)
    index_elve = calorie_list.index(max_calorie) + 1

    return max_calorie, index_elve


calorie, elve = Max_Calories_Elves(challenge_input)
print(f"Answer: {calorie}")


def Top_Calories_Elves(challenge_input_variable, top=3):
    """
    input: string with \n and \n\n
    parameters: number of top elves to count calories for
    output: max calories and index of elve
    """
    input_example_elves = challenge_input_variable.split("\n\n")
    calorie_list = [
        sum(list(map(int, number.split("\n")))) for number in input_example_elves
    ]

    top_calorie = 0
    for i in range(top):
        max_calorie = max(calorie_list)
        index_elve = calorie_list.index(max_calorie)
        top_calorie += max_calorie
        del calorie_list[index_elve]

    return top_calorie


top_calorie = Top_Calories_Elves(challenge_input, 3)
print(f"Answer: {top_calorie}")
