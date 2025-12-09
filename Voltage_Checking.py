from Batteries import *
from Find_Highest_Digit import *


total_voltage = 0

for pack in battery_packs:
    stringy_battery = str(pack)
    starting_point = 0
    stopping_point = len(stringy_battery) - 11
    highest_digits = []

    digits = []
    for digit in stringy_battery:
        digits.append(int(digit))
    
    
    for r in range (0, 12):
        results = find_highest_digit(digits, starting_point, stopping_point)
        highest_digits.append(str(results['highest_digit']))
        starting_point = results['new_starting_point']
        stopping_point = results['new_stopping_point']


    
    highest_voltage = "".join(highest_digits)
    total_voltage += int(highest_voltage)

 
print(total_voltage)
    
