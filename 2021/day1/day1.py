def is_increase(previous,current):
    if current > previous:
        return True
    else:
        return False


def find_total_increase(lines):
    result = 0
    for idx, num in enumerate(lines):
        if is_increase(lines[idx-1],lines[idx]):
            result = result + 1 
        else:
            continue 
    return result

with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

def get_sum_of_every_three_num(lines):
    sum_list = []
    for idx, num in enumerate(lines):
        if idx < len(lines) - 2:
            s = lines[idx] + lines[idx + 1] + lines[idx + 2]
            print(s)
            sum_list.append(s)
    return sum_list


# print(find_total_increase(lines))

l = [199,200,208,210]
three_sum_lst = get_sum_of_every_three_num(lines)
print(get_sum_of_every_three_num(lines))

print(find_total_increase(three_sum_lst))

