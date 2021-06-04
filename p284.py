
# input
ps = input().split()

# process
res_lt = []
len_half_ps = len(ps)//2
c1, c2 = ps[:len_half_ps], ps[len_half_ps:]
for i in range(len_half_ps):
    res_lt.append(c1[i])
    res_lt.append(c2[i])
res = ' '.join(res_lt)

# output
print(res)
