from ID_Collection import *

invalid_IDs = []

for product in products:
    for ID in range (product["min"], product["max"]+1):
        
        stringy_ID = str(ID)

        if len(stringy_ID) % 2 == 0:
            new_list = list(stringy_ID)
            print(new_list)           

