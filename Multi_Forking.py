from Wrapping_Paper import *
from Forklift import *


has_new_shelf = True
current_shelves = []
collected_paper = 0

total_collected_paper = 0


total_collected_paper, current_shelves, has_new_shelf = forklift(shelves)

while has_new_shelf is True:
    collected_paper, current_shelves, has_new_shelf = forklift(current_shelves)

    if collected_paper > 0:
        has_new_shelf = True
        total_collected_paper += collected_paper
    else:
        has_new_shelf = False
    

print(total_collected_paper)