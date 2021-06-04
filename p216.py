# the sample output 2 is in a wrong form
import json

# input
lib = json.loads(input())

# process
alphabets = {i: chr(65+i) for i in range(26)}


def to_26(num):
    if not num:
        return 'A'
    n_26 = ''
    while num:
        r = num % 26
        n_26 = alphabets[r] + n_26
        num //= 26
    return n_26


def pos_padding(num, t):
    len_n = len(num)
    amount = 3-len_n if t == "name" or t == "cat" else 4-len_n
    for i in range(amount):
        num = 'A' + num
    return num


for value in lib.values():
    len_val = len(value)
    for i in range(len_val):
        value[i] = pos_padding(to_26(int(value[i][:3])), "name") +\
            pos_padding(to_26(int(value[i][3:6])), "cat") +\
            pos_padding(to_26(int(value[i][6:])), "in")

# output
for key, value in lib.items():
    print(key, end=' ')
    print(value)
