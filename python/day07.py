# load data
with open("../input/day07_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("../input/day07_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def part1(challenge_input):
    cwd = ""
    directories = {}
    directories_in_path = []
    for line in challenge_input.splitlines():
        line = line.split()
        if (line[0] == "$") & (line[1] == "cd"):
            if line[2] == "/":  # "$ cd /"
                cwd = "/"
                directories_in_path = ["/"]
            elif line[2].isalpha():  # "$ cd a"
                if cwd == "/":
                    cwd += line[2]
                    directories_in_path.append(cwd)
                else:
                    cwd += "/" + line[2]
                    directories_in_path.append(cwd)
            elif line[2] == "..":  # "4 cd .."
                directories_in_path.pop()
                cwd = directories_in_path[-1]
        elif line[0].isdigit():
            for directory in directories_in_path:
                directories.setdefault(directory, 0)
                directories[directory] += int(line[0])

    return sum([size for size in list(directories.values()) if size <= 100000])


print(part1(challenge_input))


def part2(challenge_input):
    total_space = 70000000
    needed_space = 30000000
    cwd = ""
    directories = {}
    directories_in_path = []
    for line in challenge_input.splitlines():
        line = line.split()
        if (line[0] == "$") & (line[1] == "cd"):
            if line[2] == "/":  # "$ cd /"
                cwd = "/"
                directories_in_path = ["/"]
            elif line[2].isalpha():  # "$ cd a"
                if cwd == "/":
                    cwd += line[2]
                    directories_in_path.append(cwd)
                else:
                    cwd += "/" + line[2]
                    directories_in_path.append(cwd)
            elif line[2] == "..":  # "4 cd .."
                directories_in_path.pop()
                cwd = directories_in_path[-1]
        elif line[0].isdigit():
            for directory in directories_in_path:
                directories.setdefault(directory, 0)
                directories[directory] += int(line[0])

    root_size = max([size for size in list(directories.values())])
    current_free_space = total_space - root_size
    needed_cleaning = needed_space - current_free_space

    return min([size for size in list(directories.values()) if size >= needed_cleaning])


print(part2(challenge_input))
