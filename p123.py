
# input
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# process


def gcd(l1, l2):
    def inner(a, b):
        if not a % b:
            return b
        return inner(b, a % b)

    res_lt = []
    for i in range(len(l1)):
        res_lt.append(inner(l1[i], l2[i]))
    return res_lt


result = gcd(l1, l2)

# output
print(result)
