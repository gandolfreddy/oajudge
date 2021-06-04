
# input
l = int(input())
w = int(input())

# process & output
for i in range(w):
    for j in range(l):
        if i % 2 and j % 2 or not i % 2 and not j % 2:
            print('+', end='')
        elif i % 2 and not j % 2 or not i % 2 and j % 2:
            print('-', end='')
    if i < w-1:
        print()
