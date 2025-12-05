class DigitTracker:

    def __init__(self):
        self.counter = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

    def count_digit(self, digit):
        digit = str(digit)
        if digit in self.counter:
            self.counter[digit] += 1
    
    def check_repeats(self):
        for digit in self.counter:
            if self.counter[digit]:
                print (self.counter[digit])




test = DigitTracker()

test.count_digit(5)
test.count_digit("5")
test.count_digit(7)

print(test.counter)
test.check_repeats()