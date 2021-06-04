
# input
s = input()
n_s = s.replace("max_sort_num(", '').replace(")", '')

# process


def max_sort_num(n_s):
    max_n = int(''.join(sorted(list(n_s), reverse=True)))
    return max_n


result = max_sort_num(n_s)

# output
print(result)
