
# input & process
def multi_sort(idn):
    return tuple(idn[1:])


building = {'A': 2, 'B': 1, 'C': 0}

n = int(input())
ids = []
for i in range(n):
    idn = input().split()
    idn[1] = building[idn[1]]
    idn[2] = int(idn[2])
    if idn[2] >= 10:
        idn[2] = 2
    elif idn[2] >= 5:
        idn[2] = 1
    else:
        idn[2] = 0
    idn[3] = int(idn[3]) % 2
    ids.append(idn)

result = sorted(ids, key=multi_sort, reverse=True)

# output
for item in result:
    print(item[0])
