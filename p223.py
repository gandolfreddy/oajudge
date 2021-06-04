
# input
s = input().split()
v = input().split()
o = input().split()

# process & output
len_s, len_v, len_o = len(s), len(v), len(o)
for i in range(len_s):
    for j in range(len_v):
        for k in range(len_o):
            print(f"{s[i]} {v[j]} {o[k]}")
