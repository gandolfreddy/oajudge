
# input
colas = int(input())
get_one_free = int(input())

# process
total = 0
while colas > 0:
    total += colas
    colas //= get_one_free

# output
print(total)
