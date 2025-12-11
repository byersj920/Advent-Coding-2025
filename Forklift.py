from Wrapping_Paper import *
from Check_For_Paper import *

#This is the shelf we are currently looking at.
row = 0
accessible_papers = 0

for shelf in shelves:

    if row == 0:
        above_shelf = ""
    else:
        above_shelf = shelves[row-1]


    try:
        below_shelf = shelves[row+1]
    except Exception:
        below_shelf = ""


    print(above_shelf)
    print(shelf)
    print(below_shelf)
    valid_papers = check_for_paper(above_shelf,shelf,below_shelf)
    print(valid_papers)
    accessible_papers += valid_papers

    row += 1


print(accessible_papers)


