
# input
n = int(input())

# process
ns = []
for i in range(4):
    if n % 2:
        n = n*3 + 1
    else:
        n //= 2
    ns.append(str(n))
    if n == 1:
        break
res = ','.join(ns)

# output
print(res)
