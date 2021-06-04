
# input
lt = list(map(int, input().split()))

# process
odd_n = None
st = set(lt)
for n in st:
    if lt.count(n) % 2:
        odd_n = n
        break

# output
print(odd_n)
