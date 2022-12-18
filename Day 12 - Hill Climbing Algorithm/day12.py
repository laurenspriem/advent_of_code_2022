# load data
with open("Day 12 - Hill Climbing Algorithm/input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read()
with open("Day 12 - Hill Climbing Algorithm/input.txt", encoding="utf-8") as f:
    challenge_input = f.read()

from heapq import heapify, heappop
from math import inf
from tqdm import tqdm


def relax(u, v, Q, shortest, pred):
    try:
        index_v = [x[1] for x in Q].index(v)
        if u[0] + 1 < Q[index_v][0]:
            Q[index_v][0] = u[0] + 1
            heapify(Q)
            shortest[v] = u[0] + 1
            pred[v] = u
    except ValueError as ve:
        pass

    return Q, shortest, pred


def part1(challenge_input_variable):
    alphabet_height = "abcdefghijklmnopqrstuvwxyz"
    Q, shortest, pred, height = [], {}, {}, {}
    for y, row in enumerate(challenge_input_variable.splitlines()):
        for x, alpha in enumerate(row):
            pred[(y, x)] = None
            if alpha == "S":
                S = (y, x)
                shortest[(y, x)] = 0
                Q.append([0, (y, x)])
                height[(y, x)] = 0
            elif alpha == "E":
                E = (y, x)
                shortest[(y, x)] = inf
                Q.append([inf, (y, x)])
                height[(y, x)] = 25
            else:
                shortest[(y, x)] = inf
                Q.append([inf, (y, x)])
                height[(y, x)] = alphabet_height.find(alpha)
    heapify(Q)
    while Q:
        u = heappop(Q)
        adjacents = [
            (u[1][0] + 1, u[1][1]),
            (u[1][0] - 1, u[1][1]),
            (u[1][0], u[1][1] + 1),
            (u[1][0], u[1][1] - 1),
        ]
        for v in adjacents:
            try:
                if height[u[1]] + 1 >= height[v]:
                    Q, shortest, pred = relax(u, v, Q, shortest, pred)
            except KeyError as ke:
                continue

    return shortest[E]


print(f"Answer: {part1(challenge_input)}")


def part2(challenge_input_variable):
    alphabet_height = "abcdefghijklmnopqrstuvwxyz"
    all_a = [
        (y, x)
        for y, row in enumerate(challenge_input_variable.splitlines())
        for x, alpha in enumerate(row)
        if alpha == "a"
    ]
    all_shortest = {}
    for a in tqdm(all_a):
        Q, shortest, pred, height = [], {}, {}, {}
        for y, row in enumerate(challenge_input_variable.splitlines()):
            for x, alpha in enumerate(row):
                pred[(y, x)] = None
                if (y, x) == a:
                    shortest[(y, x)] = 0
                    Q.append([0, (y, x)])
                    height[(y, x)] = 0
                elif alpha == "E":
                    E = (y, x)
                    shortest[(y, x)] = inf
                    Q.append([inf, (y, x)])
                    height[(y, x)] = 25
                else:
                    shortest[(y, x)] = inf
                    Q.append([inf, (y, x)])
                    height[(y, x)] = alphabet_height.find(alpha)
        heapify(Q)
        while Q:
            u = heappop(Q)
            adjacents = [
                (u[1][0] + 1, u[1][1]),
                (u[1][0] - 1, u[1][1]),
                (u[1][0], u[1][1] + 1),
                (u[1][0], u[1][1] - 1),
            ]
            for v in adjacents:
                try:
                    if height[u[1]] + 1 >= height[v]:
                        Q, shortest, pred = relax(u, v, Q, shortest, pred)
                except KeyError as ke:
                    continue
        all_shortest[a] = shortest[E]

    return min(all_shortest.values())


print(f"Answer: {part2(challenge_input)}")
