
# input
s1 = input()
s2 = input()

# process
res_s = ''
i, j = 0, 0
len_s1, len_s2 = len(s1), len(s2)
while i < len_s1 and j < len_s2:
    res_s += s1[i] + s2[j]
    i, j = i+1, j+1
if i < len_s1:
    res_s += s1[i:]
if j < len_s2:
    res_s += s2[j:]

# output
print(res_s)
