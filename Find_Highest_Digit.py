

def find_highest_digit (digits: list, starting_point: int, stopping_point: int):

    results = {"highest_digit": 0, "new_starting_point": starting_point, "new_stopping_point": stopping_point + 1}

    for r in range (starting_point, stopping_point):
        if digits[r] > results["highest_digit"]:
            results["highest_digit"] = digits[r]
            results["new_starting_point"] = r + 1
        
        if results["highest_digit"] == 9:
            return results
    

    return results
