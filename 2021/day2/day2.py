with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def get_final_position(lst):
    horizontal = 0
    depth = 0
    for l in lst:
        x = l.split()
        if x[0] == 'forward':
            horizontal = horizontal + int(x[1])
        elif x[0] == 'down':
            depth = depth + int(x[1])
        elif x[0] == 'up':
            depth = depth - int(x[1])
    return horizontal * depth

print(get_final_position(lines))
