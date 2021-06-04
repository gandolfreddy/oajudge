
# input
l = input().split()

# process
result = sorted(l, key=lambda elem: elem[::-1])

# output
print(result)
