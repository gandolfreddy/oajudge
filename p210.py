# need to modify the description
# and the sample output 2 is in a wrong form

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
    pre_ch = bin_n[0]
    bin_lt = [pre_ch]
    for i in range(1, len_bin):
        if bin_n[i] != pre_ch:
            pre_ch = bin_n[i]
            bin_lt.append(pre_ch)
    return list(map(int, bin_lt))


result = to_binary(n)

# output
print(result)
