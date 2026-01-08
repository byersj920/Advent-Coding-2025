from Puzzle_Input import *

final_pantry = []
final_pantry.append(valid_ranges[0])
golden_range = valid_ranges[1]
temp_pantry = []

for id_range in valid_ranges:

    if id_range['min'] <= golden_range['min'] and id_range['max'] >= golden_range['max']:
        golden_range = id_range
        print(golden_range)
        continue
    

    if id_range['min'] < golden_range['min'] and id_range['max'] <= golden_range['max'] and id_range['max'] >= golden_range['min']:
        golden_range['min'] = id_range['min']
        print(golden_range)
    
    if id_range['max'] > golden_range['max'] and id_range['min'] <= golden_range['max'] and id_range['min'] >= golden_range['min']:
        golden_range['max'] = id_range['max']
        print(golden_range)
    


print(f'The final range is {golden_range}.')

