
# input
l = list(map(int, input().split()))

# process


def max_mul(lt):
    max_n = -100000000
    for i in range(1, len(lt)):
        pre_n = lt[i] * lt[i-1]
        if max_n < pre_n:
            max_n = pre_n
    return max_n


result = max_mul(l)

# output
print(result)
