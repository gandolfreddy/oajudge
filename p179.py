# input
s_lt = list(input())

# process
len_s = len(s_lt)
for i in range(len_s):
    s_lt[i] = chr(ord(s_lt[i])-(i+1))
res_s = ''.join(s_lt)

# output
print(res_s)
