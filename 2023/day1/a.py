def find_integer(s):
    left, right = 0, len(s) - 1
    left_integer, right_integer = None, None

    while left_integer is None or right_integer is None:
        if s[left].isdigit() and left_integer is None:
            left_integer = int(s[left])

        if s[right].isdigit() and right_integer is None:
            right_integer = int(s[right])

        if left_integer is not None and right_integer is not None:
            return int(str(left_integer) + str(right_integer))
        left += 1
        right -= 1

    if left_integer is not None and right_integer is not None:
        print(f"Found integers: Left - {left_integer}, Right - {right_integer}")
    else:
        print("Could not find integers from both ends")

total = 0
with open('input.txt', 'r') as f:
    lines = f.read().split()

    for line in lines:
        print(line)
        total = total + find_integer(line)
        print(f"The number is {find_integer(line)}")
        print(f"Total is {total}")


