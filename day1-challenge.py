#
# Created by David Clark on 12/06/2023
# 
#
import re




with open("input.txt", "r") as f:
    lines = f.readlines()
    new_lines = ' '.join(lines).replace('\n','').split()
# for part 2, TBD
numChars = ['one','two','three','four','five','six','seven','eight','nine']


def find_first_last_occurrences(lines):
    results = []

    for line in new_lines:
        # Find all occurrences of numbers in the string
        numbers = re.findall(r'\d', line)
        print(numbers)

        if numbers:
            # Extract the first and last occurrences of a number
            first_occurrence = (numbers[0])
            last_occurrence = (numbers[-1])

            results.append(first_occurrence + last_occurrence)
        else:
            # Handle the case where no numbers are found in the string
            results.append(None)

    return results


occurrences = find_first_last_occurrences(lines)
sum = 0
for occurrence in occurrences:
    sum = sum + int(occurrence)
print(sum)



