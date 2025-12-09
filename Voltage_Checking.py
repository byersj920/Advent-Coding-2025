from Batteries import *


total_voltage = 0

for pack in battery_packs:
    stringy_battery = str(pack)
    highest_voltage = 0
    stopping_point = len(stringy_battery) - 13
    starting_point = 0

    digits = []
    for digit in stringy_battery:
        digits.append(int(digit))
    
    

    for r in range (starting_point, stopping_point):

        




    
    total_voltage += highest_voltage

 
print(total_voltage)
    
