from Check_For_Paper import *

def forklift(shelves: list):

    accessible_paper_count = 0
    new_row = []
    new_shelf = []
    has_something_changed = False
    

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


        accessible_paper_count, new_row, has_something_changed = check_for_paper(above_shelf,shelf,below_shelf)
        accessible_papers += accessible_paper_count
        new_row = ''.join(new_row)
        new_shelf.append(new_row)

        row += 1


    return(accessible_papers, new_shelf, has_something_changed)

