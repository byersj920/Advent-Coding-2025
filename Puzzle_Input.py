puzzle_input = """3-5
10-14
16-20
12-18"""


puzzle_input = puzzle_input.split('\n\n')

valid_ranges_strings = puzzle_input[0].split('\n')
<<<<<<< HEAD

=======
>>>>>>> 736f9661b8aed972cc0cf716cd55598d52cac480

valid_ranges = []
ingredients = []

for id_range in valid_ranges_strings:
    new_range = {}
    splitRange = id_range.split('-')
    
    new_range["min"] = int(splitRange[0])
    new_range["max"] = int(splitRange[1])
    valid_ranges.append(new_range)

<<<<<<< HEAD

print (valid_ranges)


=======
>>>>>>> 736f9661b8aed972cc0cf716cd55598d52cac480

