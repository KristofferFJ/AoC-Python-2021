import read_functions

input = read_functions.read_as_strings("input.txt")
input_output_numbers = [[j[0].split(), j[1].split()] for j in [i.split("|") for i in input]]


def determine_top(one, seven):
    for letter in seven:
        if letter not in one:
            return letter


def contains_letters(this, that):
    for letter in that:
        if letter not in this:
            return False
    return True


def contains_letters(this, that):
    for letter in that:
        if letter not in this:
            return False
    return True


class Wiring:
    def __init__(self, input_output):
        self.input = input_output[0]
        self.output = input_output[1]
        remaining_letters = self.input
        one = self.find_one()
        remaining_letters.remove(one)
        seven = self.find_seven()
        remaining_letters.remove(seven)
        four = self.find_four()
        remaining_letters.remove(four)
        eight = self.find_eight()
        remaining_letters.remove(eight)
        six = self.find_six(one)
        remaining_letters.remove(six)
        nine = self.find_nine(four)
        remaining_letters.remove(nine)
        zero = [i for i in remaining_letters if len(i) == 6][0]
        remaining_letters.remove(zero)
        five = self.find_five(six)
        remaining_letters.remove(five)
        three = self.find_three(one)
        remaining_letters.remove(three)
        two = remaining_letters[0]

        self.numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    def determine_output_numbers(self):
        wired_numbers = ""
        for number in self.output:
            wired_numbers += str(self.find_matching_number(number))
        return int(wired_numbers)

    def find_matching_number(self, number):
        for potential_match in self.numbers:
            if len(potential_match) == len(number) and contains_letters(potential_match, number):
                return self.numbers.index(potential_match)

    def find_one(self):
        return [i for i in self.input if len(i) == 2][0]

    def find_seven(self):
        return [i for i in self.input if len(i) == 3][0]

    def find_four(self):
        return [i for i in self.input if len(i) == 4][0]

    def find_eight(self):
        return [i for i in self.input if len(i) == 7][0]

    def find_six(self, one):
        return [i for i in self.input if len(i) == 6 and not contains_letters(i, one)][0]

    def find_nine(self, four):
        return [i for i in self.input if len(i) == 6 and contains_letters(i, four)][0]

    def find_five(self, six):
        return [i for i in self.input if len(i) == 5 and contains_letters(six, i)][0]

    def find_three(self, one):
        return [i for i in self.input if len(i) == 5 and contains_letters(i, one)][0]


sum_of_output = 0
for input_output in input_output_numbers:
    wiring = Wiring(input_output)
    sum_of_output += wiring.determine_output_numbers()

print(sum_of_output)