# need to modify the description

# input
n = int(input().replace("to_binary(", '').replace(")", ''))

# process


def to_binary(n):
    bin_n = ''
    while n:
        r = n % 2
        bin_n = str(r) + bin_n
        n //= 2
    len_bin = len(bin_n)
    pre_n = bin_n[0]
    bin_lt = [pre_n]
    len_n = 1
    for i in range(1, len_bin):
        if bin_n[i] != pre_n:
            if len_n > 1:
                bin_lt.append(len_n)
            len_n = 1
            pre_n = bin_n[i]
            bin_lt.append(pre_n)
        else:
            len_n += 1
    if len_n > 1:
        bin_lt.append(len_n)
    return list(map(int, bin_lt))


result = to_binary(n)

# output
print(result)
