"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

TEST_DATA = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()

letters = set('abcdefghijklmnopqrstuvwxyz')


def get_input():
    f = open('2023.01.input')
    lines = f.read().strip().split('\n')
    return [e.strip() for e in lines if e.strip()]



def extract_number_part(s):
    numerals = [e for e in s if e not in letters]
    calibration_value = int(numerals[0] + numerals[-1])
    return calibration_value

def process_line(s):

    def subprocess(processed_chars, unprocessed_chars):
        if len(unprocessed_chars) == 0:
            return processed_chars
        else:
            return subprocess(processed_chars, unprocessed_chars)

    #processed_line = subprocess('', s)
    return extract_number_part(s)


NUMERAL_TUPLES = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ]

def convert_spelled_out_numerals(s):
    if s == '':
        return ''
    else:
        for n, d in spelled_out_numerals:
            if s.startswith(n):
                letter_count = len(n)
                ns = s[letter_count:]
                return d + convert_spelled_out_numerals(ns)

    return s[0] + convert_spelled_out_numerals(s[1:])




def part1():
    lines = get_input()
    numbers = [extract_number_part(line) for line in lines]
    return numbers

def part2():
    lines = get_input()
    lines2 = [convert_spelled_out_numerals(line) for line in lines]
    numbers = [extract_number_part(line) for line in lines2]
    return numbers


def test():
    return parse(TEST_DATA)


if __name__ == '__main__':
    for line in TEST_DATA.split('\n'):
        print(process_line(line))    

