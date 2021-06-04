from itertools import permutations


# input
t = list(map(int, input().split()))

# process
t.sort()
p = list(permutations(t))
len_p = len(p)
max_t = None
for i in range(len_p):
    if (p[i][0] == 2 and p[i][1] <= 3 or p[i][0] <= 1 and p[i][1] <= 9) and \
            p[i][2] <= 5 and p[i][3] <= 9:
        max_t = p[i]
    else:
        p[i] = None

result = f"{max_t[0]}{max_t[1]}:{max_t[2]}{max_t[3]}" if max_t else "error"

# output
print(result)
