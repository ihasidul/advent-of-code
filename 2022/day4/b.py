
def range_inside_other(r1, r2):
	return (int(r1[0]) >= int(r2[0]) and int(r1[1]) <= int(r2[1])) or (int(r2[0]) >= int(r1[0]) and int(r2[1]) <= int(r1[1]))

def overlap_at_all(r1, r2):
    return (int(r1[0]) <= int(r2[0]) and int(r1[1]) >= int(r2[0])) or (int(r2[0]) <= int(r1[0]) and int(r2[1]) >= int(r1[0]))

# with open("demo-input.txt") as input_file:
with open("input.txt") as input_file:
  input = input_file.readlines()

pairs_list = []
num_full_containments = 0

for line in input:
  pairs_list.append(line.strip())

for pairs in pairs_list:
    both_pairs = pairs.split(",")
    pair_1 = both_pairs[0].split("-")
    pair_2= both_pairs[1].split("-")
    if range_inside_other(pair_1, pair_2):
        num_full_containments += 1
    elif overlap_at_all(pair_1, pair_2):
        num_full_containments += 1
print(num_full_containments)
