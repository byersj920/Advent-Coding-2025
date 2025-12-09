

def find_highest_digit (digits: list, starting_point: int, stopping_point: int):

    highest_digit = 0
    new_starting_point = 0
    new_stopping_point = stopping_point - 1

    for r in range (starting_point, stopping_point):
        if digits[r] > highest_digit:
            highest_digit = digits[r]
            new_starting_point = r
        
        if highest_digit == 9:
            return highest_digit, new_starting_point, new_stopping_point
    

    return highest_digit, new_starting_point, new_stopping_point
