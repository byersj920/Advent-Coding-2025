from Puzzle_Input import *

final_pantry = []
final_pantry.append(valid_ranges[0])

for id_range in valid_ranges:
    
    min_value_inserted = False
    max_value_inserted = False

    for shelf in final_pantry:

        if id_range['min'] <= shelf['min'] and id_range['max'] >= shelf['min']:
            shelf['min'] = id_range['min']
            min_value_inserted = True
            print(final_pantry)
        if id_range['max'] >= shelf['max'] and id_range['min'] <= shelf['max']:
            shelf['max'] = id_range['max']
            max_value_inserted = True
            print(final_pantry)

    if min_value_inserted == False and max_value_inserted == False:
        final_pantry.append(id_range)
        print(final_pantry)


print(final_pantry)