from Puzzle_Input import *
from Fit_Check import *


repeat_flag = True
old_pantry = valid_ranges


while repeat_flag == True:

    repeat_flag = False
    final_pantry = []
    golden_range = valid_ranges[0]

    for id_range in valid_ranges:

        silver_range = golden_range

        silver_range = Fit_Check(id_range, golden_range)

        if silver_range == 'Outside Range!':
            final_pantry.append(id_range)
        else:
            golden_range = silver_range
        
        
    if 

    print(f'The final range is {golden_range}.')
    print(final_pantry)

