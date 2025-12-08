from Batteries import *

total_voltage = 0
voltage_list = []

for pack in battery_packs:
    stringy_battery = str(pack)
    digit_list = []
    highest_voltage = 0


    for digit in stringy_battery:
        digit_list.append(digit)

    starting_range = 0
    max_voltage = 0

    for digit in digit_list:

        for num in range (starting_range, len(digit_list)-1):
            voltage_combo = int(digit_list[starting_range] + digit_list[num+1])
            if voltage_combo > max_voltage:
                max_voltage = voltage_combo
        
        starting_range += 1
    
    total_voltage += max_voltage


print(total_voltage)
    
