# Notes:
# The first half of the characters represent items in the first compartment
# The second half of the characters represent items in the second compartment
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# One dictionaries are created to store the priorities of each item type.
PRIORITY_DICT = {"a":1,
                 "b":2,
                 "c":3,
                 "d":4,
                 "e":5,
                 "f":6,
                 "g":7,
                 "h":8,
                 "i":9,
                 "j":10,
                 "k":11,
                 "l":12,
                 "m":13,
                 "n":14,
                 "o":15,
                 "p":16,
                 "q":17,
                 "r":18,
                 "s":19,
                 "t":20,
                 "u":21,
                 "v":22,
                 "w":23,
                 "x":24,
                 "y":25,
                 "z":26,
                 "A":27,
                 "B":28,
                 "C":29,
                 "D":30,
                 "E":31,
                 "F":32,
                 "G":33,
                 "H":34,
                 "I":35,
                 "J":36,
                 "K":37,
                 "L":38,
                 "M":39,
                 "N":40,
                 "O":41,
                 "P":42,
                 "Q":43,
                 "R":44,
                 "S":45,
                 "T":46,
                 "U":47,
                 "V":48,
                 "W":49,
                 "X":50,
                 "Y":51,
                 "Z":52}
sum_of_priorities = 0
def split_string(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

with open('input.txt', 'r') as f:
    for i in f:
        s1, s2 = split_string(i)
        common_character = ''.join(set(s1).intersection(s2))
        sum_of_priorities += PRIORITY_DICT[common_character]
        # print(PRIORITY_DICT[common_character])
        # print(common_character)
print(sum_of_priorities)
