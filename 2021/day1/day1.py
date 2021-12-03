result = 0
def is_increase(previous,current):
    if current > previous:
        return True
    else:
        return False

with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

print(type(lines[0]))

for idx, num in enumerate(lines):
    if is_increase(lines[idx-1],lines[idx]):
        result = result + 1 
    else:
        continue 
print(result)
