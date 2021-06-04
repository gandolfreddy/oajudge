
# input
n = int(input())

# process
alphabets = {i: chr(65+i) for i in range(26)}


def to_26(num):
    if not num:
        return 'A'
    n_26 = ''
    while num:
        r = num % 26
        n_26 = alphabets[r] + n_26
        num //= 26
    return n_26


result = to_26(n)

# output
print(result)
