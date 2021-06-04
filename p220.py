# the sample input1 & input2 are in the wrong form

# input
n = int(input())
grid = []
for i in range(n):
    row = list(map(int, input().split(',')))
    grid.append(row)

# process
direct = ((1, 0), (-1, 0), (0, -1), (0, 1))


def dfs(i, j):
    grid[i][j] = 0
    cnt = 1
    for d in direct:
        dx, dy = j+d[0], i+d[1]
        if 0 <= dx and dx < n and 0 <= dy and dy < n and grid[dy][dx]:
            cnt += dfs(dy, dx)
    return cnt


max_cnt, cnt = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            cnt = dfs(i, j)
            max_cnt = max(max_cnt, cnt)

# output
print(f"max size is {max_cnt}")
