
# input
bento = list(input())
n_a = int(input())
n_b = int(input())

# process
while n_a and bento[0] == 'A' or n_b and bento[0] == 'B':
    if n_a and bento[0] == 'A':
        bento.pop(0)
        n_a -= 1
    elif n_b and bento[0] == 'B':
        bento.pop(0)
        n_b -= 1
remain = n_a or n_b

# output
print(remain)
