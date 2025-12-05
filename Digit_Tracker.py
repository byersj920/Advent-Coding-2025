class DigitTracker:

    def __init__(self):
        self.counter = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

    def count_digit(self, digit):
        digit = str(digit)
        if digit in self.counter:
            self.counter[digit] += 1

    def delete_empties(self):
        deletion_list = []
        for digit in self.counter:
            if self.counter[digit] == 0:
                deletion_list.append(digit)
        for num in deletion_list:
            self.counter.pop(num)
    
    def check_repeats(self):
        check_list = []
        for digit in self.counter:
            check_list.append(self.counter[digit])
        
        for num in check_list:
            if num != check_list[0]:
                return False
        
        return True


test = DigitTracker()

test.count_digit(5)
test.count_digit("5")
test.count_digit(7)

print(test.counter)
test.delete_empties()
print(test.counter)
print(test.check_repeats())