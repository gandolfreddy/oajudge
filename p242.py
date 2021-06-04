
# input
lim = int(input())
n = int(input())
lt = []
for i in range(n):
    item, p, w = input().split()
    p, w = int(p), int(w)
    lt.append((item, p/w, w))

# process
lt.sort(key=lambda item: item[2], reverse=False)
lt.sort(key=lambda item: item[1], reverse=True)
capacity = lim
backpack = ''
while lt:
    if lt[0][2] <= capacity:
        capacity -= lt[0][2]
        backpack += lt[0][0]
    lt.pop(0)

# output
for elem in backpack:
    print(elem)
