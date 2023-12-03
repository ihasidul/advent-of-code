import re

with open('input.txt', 'r') as f:
    strings = f.read().split()

word_to_digit = {
    'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r',
    'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
}
count = 0
modified_strings = []  

for string in strings:
    for word, replacement in word_to_digit.items():
        string = string.replace(word, replacement)
    
    numbers = re.findall(r"\d", string)
    first_number = int(numbers[0])
    last_number = int(numbers[-1])

    count += first_number * 10 + last_number
    modified_strings.append(string)  

print(count)