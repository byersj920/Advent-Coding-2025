
test_number = '526314178'

varA = 0
varB = 1
varC = 2
varD = 3
varE = 4
varF = 5
varG = 6

stopping_value = len(test_number)-1

highest_combo = 0

while varA != stopping_value-2:
    new_combo = int(test_number[varA] + test_number[varB] + test_number[varC])
    if new_combo > highest_combo:
        highest_combo = new_combo
    
    varC += 1

    if varC > stopping_value:
        varB += 1
        varC = varB + 1
    
    if varB > stopping_value-1:
        varA +=1
        varB = varA+1
        varC = varB+1


print(highest_combo)



