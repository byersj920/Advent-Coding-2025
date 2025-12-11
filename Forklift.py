from Check_For_Paper import *


def forklift(shelves: list):
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


        accessible_papers += check_for_paper(above_shelf,shelf,below_shelf)

        row += 1


    print(accessible_papers)



