# load data
with open("../input/day09_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("../input/day09_input.txt", encoding="utf-8") as f:
    challenge_input = f.read()


def move_T(H=[0, 0], T=[0, 0], T_locations=[], distance=1):
    [Hx, Hy], [Tx, Ty] = H, T
    if (Hx == Tx) and (Hy != Ty) and (abs(Hy - Ty) > distance):
        T[1] += (Hy - Ty) // abs(Hy - Ty)
        T_locations.append(tuple(T))
    if (Hx != Tx) and (Hy == Ty) and (abs(Hx - Tx) > distance):
        T[0] += (Hx - Tx) // abs(Hx - Tx)
        T_locations.append(tuple(T))
    if (Hx != Tx) and (Hy != Ty) and ((abs(Hx - Tx) + abs(Hy - Ty)) > distance + 1):
        T[0] += (Hx - Tx) // abs(Hx - Tx)
        T[1] += (Hy - Ty) // abs(Hy - Ty)
        T_locations.append(tuple(T))
    return T, T_locations


def part1(challenge_input_variable):
    H_locations = [(0, 0)]
    T_locations = [(0, 0)]
    for move in challenge_input_variable.splitlines():
        [direction, number] = move.split()
        number = int(number)
        H_location, T_location = list(H_locations[-1]), list(T_locations[-1])
        if direction == "L":
            for _ in range(number):
                H_location[0] -= 1
                H_locations.append(tuple(H_location))
                T_location, T_locations = move_T(H_location, T_location, T_locations)
        elif direction == "R":
            for _ in range(number):
                H_location[0] += 1
                H_locations.append(tuple(H_location))
                T_location, T_locations = move_T(H_location, T_location, T_locations)
        elif direction == "U":
            for _ in range(number):
                H_location[1] += 1
                H_locations.append(tuple(H_location))
                T_location, T_locations = move_T(H_location, T_location, T_locations)
        elif direction == "D":
            for _ in range(number):
                H_location[1] -= 1
                H_locations.append(tuple(H_location))
                T_location, T_locations = move_T(H_location, T_location, T_locations)

    return len(list(set(T_locations)))


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input_variable):
    H_locations = [(0, 0)]
    Knot_locations = [[(0, 0)] for i in range(9)]
    for move in challenge_input_variable.splitlines():
        [direction, number] = move.split()
        number = int(number)
        H_location, Knot_location = list(H_locations[-1]), [
            list(locations[-1]) for locations in Knot_locations
        ]
        if direction == "L":
            for _ in range(number):
                H_location[0] -= 1
                H_locations.append(tuple(H_location))
                Knot_location[0], Knot_locations[0] = move_T(
                    H_location, Knot_location[0], Knot_locations[0]
                )
                for i in range(1, 9):
                    Knot_location[i], Knot_locations[i] = move_T(
                        Knot_location[i - 1], Knot_location[i], Knot_locations[i]
                    )
        elif direction == "R":
            for _ in range(number):
                H_location[0] += 1
                H_locations.append(tuple(H_location))
                Knot_location[0], Knot_locations[0] = move_T(
                    H_location, Knot_location[0], Knot_locations[0]
                )
                for i in range(1, 9):
                    Knot_location[i], Knot_locations[i] = move_T(
                        Knot_location[i - 1], Knot_location[i], Knot_locations[i]
                    )
        elif direction == "U":
            for _ in range(number):
                H_location[1] += 1
                H_locations.append(tuple(H_location))
                Knot_location[0], Knot_locations[0] = move_T(
                    H_location, Knot_location[0], Knot_locations[0]
                )
                for i in range(1, 9):
                    Knot_location[i], Knot_locations[i] = move_T(
                        Knot_location[i - 1], Knot_location[i], Knot_locations[i]
                    )
        elif direction == "D":
            for _ in range(number):
                H_location[1] -= 1
                H_locations.append(tuple(H_location))
                Knot_location[0], Knot_locations[0] = move_T(
                    H_location, Knot_location[0], Knot_locations[0]
                )
                for i in range(1, 9):
                    Knot_location[i], Knot_locations[i] = move_T(
                        Knot_location[i - 1], Knot_location[i], Knot_locations[i]
                    )

    return len(list(set(Knot_locations[-1])))


print(f"Answer: {part2(challenge_input)}")
