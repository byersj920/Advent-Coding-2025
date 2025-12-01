from combinations import *

sequence = sequence.split('\n')

zero_counter = 0
dial = 50

for rotation in sequence:
    rotate_amount = int(rotation[1:])
    
    if rotation.startswith('R'):
       for digit in range(0, rotate_amount):
           dial += 1
           if dial == 100:
               dial = 0
               zero_counter += 1
           
    
    if rotation.startswith('L'):
        for digit in range(0, rotate_amount):
           dial -= 1
           if dial == 0:
               zero_counter += 1
           elif dial == -1:
               dial = 99

print (zero_counter)