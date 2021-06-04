
# input
ava = int(input())
ps = list(map(int, input().split()))

# process
n_ps = [100-p for p in ps]
len_nps = len(n_ps)
max_no_rain_p = 0
max_no_rain_i = 0
for i in range(len_nps-(ava-1)):
    cur_no_rain_p = 1
    for j in range(ava):
        cur_no_rain_p *= n_ps[i+j]
    if max_no_rain_p < cur_no_rain_p:
        max_no_rain_p = cur_no_rain_p
        max_no_rain_i = i

# output
print(max_no_rain_i)
