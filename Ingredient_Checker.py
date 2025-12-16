from Puzzle_Input import *

valid_IDs = []

for id_range in valid_ranges:
    for num in range(id_range['min'], id_range['max']+1):
        
        if num in valid_IDs:
            continue
        else:
            valid_IDs.append(num)

print(len(valid_IDs))

