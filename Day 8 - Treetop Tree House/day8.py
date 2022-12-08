# load data
with open("Day 8 - Treetop Tree House/input_sample.txt") as f:
    challenge_input_sample = f.read()
with open("Day 8 - Treetop Tree House/input.txt") as f:
    challenge_input = f.read()

import numpy as np
from math import prod

def part1(challenge_input_variable):
    outer_trees = 2*(challenge_input_variable.count('\n')+1) + 2 * (len(challenge_input_variable.splitlines()[0]) -2)
    tree_array = np.fromstring(" ".join(challenge_input_variable.replace('\n','')), dtype=int, sep=' ')
    tree_array = tree_array.reshape((challenge_input_variable.count('\n')+1,len(challenge_input_variable.splitlines()[0])))
    inner_trees = 0
    
    for line_count, line in enumerate(challenge_input_variable.splitlines()):
        if line_count == 0 or line_count == challenge_input_variable.count('\n'):
            continue
        for character_count, character in enumerate(line):
            if character_count == 0 or character_count == len(line)-1:
                continue
            if max(tree_array[:line_count,character_count]) < int(character): # check above trees
                inner_trees += 1
            elif max(tree_array[line_count+1:,character_count]) < int(character): # check below trees
                inner_trees += 1
            elif max(tree_array[line_count,character_count+1:]) < int(character): # check right trees
                inner_trees += 1
            elif max(tree_array[line_count,:character_count]) < int(character): # check left trees
                inner_trees += 1

    return outer_trees + inner_trees

print(f"Answer: {part1(challenge_input)}")

def part2(challenge_input_variable):
    tree_array = np.fromstring(" ".join(challenge_input_variable.replace('\n','')), dtype=int, sep=' ')
    tree_array = tree_array.reshape((challenge_input_variable.count('\n')+1,len(challenge_input_variable.splitlines()[0])))
    inner_trees = []
    
    for line_count, line in enumerate(challenge_input_variable.splitlines()):
        for character_count, character in enumerate(line):
            inner_trees.append([0,0,0,0])

            for other_tree in np.flip(tree_array[:line_count,character_count]): # check above trees
                inner_trees[-1][0] += 1
                if other_tree >= int(character):
                    break
            
            for other_tree in np.flip( tree_array[line_count,:character_count] ): # check left trees
                inner_trees[-1][1] += 1
                if other_tree >= int(character):
                    break

            for other_tree in tree_array[line_count+1:,character_count]: # check below trees
                inner_trees[-1][2] += 1
                if other_tree >= int(character):
                    break

            for other_tree in tree_array[line_count,character_count+1:]: # check right trees
                inner_trees[-1][3] += 1
                if other_tree >= int(character):
                    break

    return max([prod(tree_sights) for tree_sights in inner_trees])

print(f"Answer: {part2(challenge_input)}")