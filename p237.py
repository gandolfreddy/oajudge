
# input
n = int(input())
dt = {}
for i in range(n):
    k, v = input().split()
    dt[k] = v
s = input().split()

# process
len_s = len(s)
for i in range(len_s):
    s[i] = dt[s[i]]
result = ' '.join(s)

# output
print(result)
