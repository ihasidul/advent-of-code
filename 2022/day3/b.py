from a import split_string, PRIORITY_DICT
#  Elves are divided into groups of three
total = 0


# with open('input.txt', 'r') as f:
#     for i in f:
#         s1, s2 = split_string(i)
with open('input.txt', 'r') as f:
    rucksacks = [line.replace('\n', '') for line in f.readlines()]

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]

    shared_item = [
        item for item in group[0]
        if item in group[1]
        and item in group[2]
    ][0]

    total += PRIORITY_DICT[shared_item]

print("Part 2",total)