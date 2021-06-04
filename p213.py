
# input
n = int(input())
t_lt = [sorted(map(int, input().split())) for i in range(n)]
t_dt = {i: 0 for i in range(24)}

# process
for t in t_lt:
    len_t = len(t)
    for i in range(len_t):
        t_dt[t[i]] += 1
t_dt = dict(filter(lambda item: item[1] >= 12, t_dt.items()))

t_lt = list(t_dt.keys())
len_t = len(t_lt)
best_t, cur_t = 0, t_lt[0]
max_len, cur_len = 0, 1
for i in range(1, len_t):
    if t_lt[i] != t_lt[i-1]+1:
        if max_len < cur_len:
            max_len, cur_len = cur_len, 1
            best_t = cur_t
        cur_t = t_lt[i]
    else:
        cur_len += 1
if cur_len > 1:
    best_t = cur_t

# output
print(best_t)
