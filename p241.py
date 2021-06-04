
# input
n = int(input())
cont = input().split()
len_c = len(cont)
cont_dt = {cont[i]: int(cont[i+1]) for i in range(0, len_c, 2)}

n = int(input())
comb_dt = {}
for i in range(n):
    comb = input().split()
    comb_dt[comb[0]] = comb[1:]

n = int(input())
wish_lt = []
for i in range(n):
    wish = input().split()
    wish_lt.append((wish[0], int(wish[1])))

# process & output
for wish in wish_lt:
    total_size = 0
    for item in comb_dt[wish[0]]:
        total_size += cont_dt[item]
    t = int(total_size/wish[1])
    print(t)
