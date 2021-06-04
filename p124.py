
# input
l = input().split()

# process
result = list(map(
    int, sorted(l, key=lambda elem: sum(map(int, list(elem))))
))

# output
print(result)
