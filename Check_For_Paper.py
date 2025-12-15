def check_for_paper(above_shelf: str = "", shelf: str = "", below_shelf: str = ""):
    
    valid_papers = 0
    new_shelf = []
    has_something_changed = False

    
    for spot in range(0, len(shelf)):
        
        if shelf[spot] != '@':
            new_shelf.append(shelf[spot])
            continue

        adjacent_papers = 0

        #top left
        try:
            if above_shelf[spot-1] == '@' and spot != 0:
                adjacent_papers += 1
        except Exception:
            pass

        #top middle
        try:
            if above_shelf[spot] == '@':
                adjacent_papers += 1
        except Exception:
            pass
        
        #top right
        try:
            if above_shelf[spot+1] == '@':
                adjacent_papers += 1
        except Exception:
            pass

        #Left
        try:
            if shelf[spot-1] == '@' and spot != 0:
                adjacent_papers += 1
        except Exception:
            pass

        #Right
        try:
            if shelf[spot+1] == '@':
                adjacent_papers += 1
        except Exception:
            pass

        #Bottom Left
        try:
            if below_shelf[spot-1] == '@' and spot != 0:
                adjacent_papers += 1
        except Exception:
            pass

        #Bottom
        try:
            if below_shelf[spot] == '@':
                adjacent_papers += 1
        except Exception:
            pass

        #Bottom Right
        try:
            if below_shelf[spot+1] == '@':
                adjacent_papers += 1
        except Exception:
            pass

        if adjacent_papers < 4:
            valid_papers += 1
            new_shelf.append('X')
            has_something_changed = True
        else:
            new_shelf.append(shelf[spot])

        
        
        

    return valid_papers, new_shelf, has_something_changed