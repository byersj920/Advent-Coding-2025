from Puzzle_Input import *

total_ranges = [{'min': 0, 'max': 0}]

for id_range in valid_ranges:
    for checked_range in total_ranges:
        if checked_range['min'] > id_range['min']:
            checked_range

print(len(valid_IDs))

