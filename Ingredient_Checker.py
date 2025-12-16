from Puzzle_Input import *

fresh_count = 0

for ingredient in ingredients:

    for range in valid_ranges:
        if ingredient >= range['min'] and ingredient <= range['max']:
            fresh_count += 1
            break


print(fresh_count)