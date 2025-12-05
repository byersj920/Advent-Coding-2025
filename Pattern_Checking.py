from ID_Collection import *
from Has_Pattern import *

invalid_ID_total = 0


for product in products:

    for ID in range (product["min"], product["max"]+1):
        
        if has_pattern(ID) == True:
            invalid_ID_total += ID



print (invalid_ID_total)
            