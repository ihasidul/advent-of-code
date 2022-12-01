elf_food = []
elf_food_cost = 0
with open('input.txt', 'r') as f:
    for i in f.readlines():
        if i != '\n':
            elf_food_cost += int(i.strip("\n"))
        else:
            elf_food.append(elf_food_cost)
            elf_food_cost = 0
print(max(elf_food))

