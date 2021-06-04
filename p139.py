from collections import deque

# input
n = int(input())

# process


def func(n):
    res = deque([('(', 1, 0)])
    while res[0][1] < n or res[0][2] < n:
        c, left, right = res.popleft()
        if left < n:
            res.append((c+'(', left+1, right))
        if right < n and left > right:
            res.append((c+')', left, right+1))
    return [r[0] for r in res]


lt = func(n)

# output
for item in lt:
    print(item)
