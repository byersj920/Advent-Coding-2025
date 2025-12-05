from ID_Collection import *
import math
from Has_Pattern import *

invalid_IDs = []


for product in products:

    for ID in range (product["min"], product["max"]+1):
        
        stringy_ID = str(ID)
        id_size = len(stringy_ID)

        for num in range (1, id_size+1):
            number_check = id_size

        if len(stringy_ID) % 2 == 0:
            new_list = list(stringy_ID)

            halfway_point = math.floor(len(new_list)/2)

            first_half = new_list[:halfway_point]
            first_half = int("".join(first_half))
            second_half = new_list[halfway_point:]
            second_half = int("".join(second_half))

            if first_half - second_half == 0:
                invalid_IDs.append(ID)

invalid_ID_total = 0

for ID in invalid_IDs:
    invalid_ID_total += ID

print (invalid_ID_total)
            