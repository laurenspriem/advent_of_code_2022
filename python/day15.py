# load data
with open("input/day15_input_sample.txt", encoding="utf-8") as f:
    challenge_input_sample = f.read().strip()
with open("input/day15_input.txt", encoding="utf-8") as f:
    challenge_input = f.read().strip()

import re
from tqdm import tqdm


def part1(challenge_input, row=2000000):
    beacons_in_row = set()
    intervals = []

    for line in challenge_input.splitlines():
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall("-?\d+", line))
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        height = distance - abs(sensor_y - row)
        if height < 0:
            continue
        left, right = sensor_x - height, sensor_x + height
        intervals.append((left, right))
        if beacon_y == row:
            beacons_in_row.add((beacon_x, beacon_y))
    intervals = sorted(intervals)
    intervals_intersect = []
    for low, high in intervals:
        if not intervals_intersect:
            intervals_intersect.append([low, high])
        elif low <= intervals_intersect[-1][1]:
            intervals_intersect[-1][1] = max(high, intervals_intersect[-1][1])
        else:
            intervals_intersect.append([low, high])
    cannot = 0
    for low, high in intervals_intersect:
        cannot += high - low + 1
    cannot = cannot - len(beacons_in_row)
    return cannot


print(f"Part1: {part1(challenge_input_sample, row=10)}")


def part2(challenge_input, row_options=4000000):

    lines = [
        list(map(int, re.findall("-?\d+", line)))
        for line in challenge_input.splitlines()
    ]
    found = False
    signal = 0
    for row in tqdm(range(row_options + 1)):
        if found == True:
            break
        intervals = []
        for sensor_x, sensor_y, beacon_x, beacon_y in lines:
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            height = distance - abs(sensor_y - row)
            if height < 0:
                continue
            left, right = sensor_x - height, sensor_x + height
            intervals.append((left, right))
        intervals = sorted(intervals)
        intervals_intersect = []
        for low, high in intervals:
            if not intervals_intersect:
                intervals_intersect.append([low, high])
            elif low <= intervals_intersect[-1][1]:
                intervals_intersect[-1][1] = max(high, intervals_intersect[-1][1])
            else:
                intervals_intersect.append([low, high])
        x = 0
        for low, high in intervals_intersect:
            if x < low:
                print(x, row)
                found = True
                signal = 4000000 * x + row
                break
            if low > row_options:
                break
            x = high + 1

    return signal


print(f"Part2: {part2(challenge_input)}")
