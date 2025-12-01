from combinations import *

sequence = sequence.split('\n')

zero_counter = 0
dial = 50

for rotation in sequence:
    rotate_amount = int(rotation[1:])
    
    if rotation.startswith('R'):
       dial += rotate_amount
       while dial >= 100:
           dial -= 100
           zero_counter += 1
           
    
    if rotation.startswith('L'):
        dial -= rotate_amount
        while dial < 0:
           dial += 100
           zero_counter += 1

    #if dial == 0:
        #zero_counter += 1

print (zero_counter)