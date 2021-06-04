# the form of sample output 2 is wrong.
from collections import deque

# input
n, m = tuple(map(int, input().split()))
cell = []
for i in range(n):
    c = [[int(i), False if int(i) != -1 else True] for i in input().split()]
    cell.append(c)
virus = int(input())

# process


def logic_and_virus(cell, virus):
    init_x, init_y = -1, -1
    for y in range(n):
        for x in range(m):
            if cell[y][x][0] == virus:
                init_x, init_y = x, y
                break
        if init_x != -1 and init_y != -1:
            break

    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque([(init_y, init_x)])
    while q:
        y, x = q.popleft()
        if not cell[y][x][1]:
            cell[y][x][0] &= virus
            cell[y][x][1] = True
            for d in dirs:
                n_x, n_y = x+d[1], y+d[0]
                if 0 <= n_x and n_x < m and 0 <= n_y and n_y < n and \
                   not cell[n_y][n_x][1]:
                    q.append((n_y, n_x))

    for i in range(n):
        cell[i] = ' '.join([str(item[0]) for item in cell[i]])

    return cell


infected_cell = logic_and_virus(cell, virus)

# output
for c in infected_cell:
    print(c)
