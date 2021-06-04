
# input
n_lt = list(input())

# process
max_i = n_lt.index(max(n_lt))
n_lt[0], n_lt[max_i] = n_lt[max_i], n_lt[0]
new_n = ''.join(n_lt)

# output
print(new_n)
