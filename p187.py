
# input
dt = {}
for i in range(20):
    chs = input().split()
    dt[chs[0]] = chs[1]
ch = input()

# process & output
ch_lt = [ch]
cur_ch = dt[ch]
while cur_ch != ch:
    ch_lt.append(cur_ch)
    cur_ch = dt[cur_ch]
res_ch = ' '.join(ch_lt)

# output
print(res_ch)
