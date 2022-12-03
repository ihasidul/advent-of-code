# Opponent's input
# A for Rock
# B for Paper
# C for Scissors

# My input
# X for Rock
# Y for Paper
# Z for Scissors

# Game
# Opponent's move ---> My move
# Draw
# A ---> X
# B ---> Y
# C ---> Z

# My win
# A ---> Y
# B ---> Z
# C ---> X
my_score = 0
win_moves_for_me = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
draw_moves_for_me = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
loose_moves_for_me = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
with open('input.txt', 'r') as f:
    for i in f:
        move = i.split()
        if move in win_moves_for_me:
            if move[1] == 'X':
                my_score += 1 + 6
            elif move[1] == 'Y':
                my_score += 2 + 6
            elif move[1] == 'Z':
                my_score += 3 + 6
        elif move in draw_moves_for_me:
            if move[1] == 'X':
                my_score += 1 + 3
            elif move[1] == 'Y':
                my_score += 2 + 3
            elif move[1] == 'Z':
                my_score += 3 + 3
        elif move in loose_moves_for_me:
            if move[1] == 'X':
                my_score += 1
            elif move[1] == 'Y':
                my_score += 2
            elif move[1] == 'Z':
                my_score += 3
print(my_score)
