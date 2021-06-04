from math import ceil

# input
region = int(input())
full_speed = int(input())
n = int(input())
registers = []
for i in range(n):
    p, x, y = input().split()
    registers.append((p, int(x), int(y)))
n = int(input())
shelters = []
for i in range(n):
    site, x, y = input().split()
    shelters.append((site, int(x), int(y)))

# process


def dis_calc(x0, y0, x1, y1):
    return ceil(((x1-x0)**2+(y1-y0)**2)**0.5)


res_lt = []
for register in registers:
    p, x0, y0 = register
    is_saved = False
    res = p
    for site in shelters:
        s, x1, y1 = site
        if dis_calc(x0, y0, x1, y1) <= full_speed:
            is_saved = True
            res += f" {s}"
    if not is_saved:
        res += " byebye"
    res_lt.append(res)

# output
for res in res_lt:
    print(res)
