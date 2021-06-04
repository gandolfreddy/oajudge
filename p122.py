
# input
l = list(map(int, input().split()))
t = int(input())

# process


def threshold(l, t):
    return list(map(lambda x: x >= t, l))


result = threshold(l, t)

# output
print(result)
